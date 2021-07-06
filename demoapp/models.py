from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Massage(models.Model):
    msg = models.CharField(max_length=256)
    msg_from = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="msg_from")
    msg_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mag_to")
    status = models.CharField(max_length=32)
    time = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ["time"]

    @property
    def formatted_time(self):
        return self.time.strftime('%b %d %I:%M %p')

    def as_dict(self):
        return {u'msg': self.msg, u'msg_from': self.msg_from.username, u'time': self.formatted_time, u'msg_to': self.msg_to.username,u"m_f_id":self.msg_from.id}

    # def __unicode__(self):
    #     return '[{time}] {msg}: {msg_from}'.format(**self.as_dict())

    # def __str__(self):
    #     """String for representing the Model object."""
    #     return self.msg


class Chenal(models.Model):

    channele_id = models.CharField(max_length=256)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")