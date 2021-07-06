import re
import json
import logging
from channels import Group
from channels.sessions import channel_session
from .models import Massage
from django.contrib.auth.models import User

log = logging.getLogger(__name__)


@channel_session
def ws_connect(message):
    # Extract the room from the message. This expects message.path to be of the
    # form /chat/{label}/, and finds a Room if the message path is applicable,
    # and if the Room exists. Otherwise, bails (meaning this is a some othersort
    # of websocket). So, this is effectively a version of _get_object_or_404.
    try:
        prefix,home, label,me = message['path'].decode('ascii').strip('/').split('/')
        if label<me:
            path=str(label)+str(me)
        else:
            path = str(me) + str(label)

        if prefix != 'chat':
            log.debug('invalid ws path=%s', message['path'])
            return

        msg_to = User.objects.get(id=label)

    except ValueError:
        log.debug('invalid ws path=%s', message['path'])
        return
    except User.DoesNotExist:
        log.debug('ws room does not exist label=%s', label)
        return

    log.debug('chat connect room=%s client=%s:%s',
              msg_to.id, message['client'][0], message['client'][1])

    # Need to be explicit about the channel layer so that testability works
    # This may be a FIXME?
    Group('home-' + str(path), channel_layer=message.channel_layer).add(message.reply_channel)

    message.channel_session['lable'] = label
    message.channel_session['me'] = me
    message.channel_session['room'] = path


@channel_session
def ws_receive(message):
    # Look up the room from the channel session, bailing if it doesn't exist
    try:
        label = message.channel_session['lable']
        msg_to =User.objects.get(id=label)
        # print(msg_to, message.channel_session['room'])
    except KeyError:
        log.debug('no room in channel_session')
        return
    except User.DoesNotExist:
        log.debug('recieved message, buy room does not exist label=%s', label)
        return

    # Parse out a chat message from the content text, bailing if it doesn't
    # conform to the expected message format.
    try:
        data = json.loads(message['text'])
    except ValueError:
        log.debug("ws message isn't json text=%s", text)
        return

    if set(data.keys()) != {'msg_from', 'msg'}:
        log.debug("ws message unexpected format data=%s", data)
        return

    if data:
        log.debug('chat message room=%s handle=%s message=%s',
                  msg_to.username, data['msg_from'], data['msg'])
        msg_from = User.objects.get(id=data['msg_from'])
        # msg_to = User.objects.get(id=slug)
        # print(data)
        m = Massage(msg_to=msg_to, msg_from=msg_from, msg=data['msg'])
        m.save()

        # See above for the note about Group
        path = message.channel_session['room']
        Group('home-' + path, channel_layer=message.channel_layer).send({'text': json.dumps(m.as_dict())})
        print(json.dumps(m.as_dict()))


@channel_session
def ws_disconnect(message):
    try:
        label = message.channel_session['label']
        user =User.objects.get(id=label)
        path = message.channel_session['room']
        Group('chat-' + path, channel_layer=message.channel_layer).discard(message.reply_channel)
    except (KeyError, User.DoesNotExist):
        pass
