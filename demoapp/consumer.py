import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import requires_csrf_token
import pusher

from .models import Massage

pusher_client = pusher.Pusher(
        app_id='1222631',
        key='fe20237c51fe22bd59b7',
        secret='981bb19f89a28fc0e80a',
        cluster='ap2',
        ssl=True
    )
def demo(request):
    data =json.loads(request.body.decode("utf-8"))

    msg_to = User.objects.get(id=data['msg_to'])
    msg_from = request.user
    m = Massage(msg_to=msg_to, msg_from=msg_from, msg=data['msg'], status="send")
    m.save()
    # m = Massage.objects.get(id=4)
    # print(data,request.user,msg_to)
    # data ={'id' : user.id, 'NAME': user.username}
    pusher_client.trigger('my-channel', str(msg_to.id), {'text': json.dumps(m.as_dict())})
    return JsonResponse({'data': data},safe=False)
    # # return HttpResponse(Massage.objects.filter(time__gt='2021-03-04 14:00', msg_from_id=3))
    #

def demo1(request,slug):
    return render(request, "chaneltesting.html")