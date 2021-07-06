from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Massage(models.Model):
    msg = models.CharField(max_length=256)
    msg_from = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="msg_from")
    msg_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mag_to")
    time = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ["time"]

    @property
    def formatted_time(self):
        return self.time.strftime('%b %d %I:%M %p')

    def as_dict(self):
        return {'msg': self.msg, 'msg_from': self.msg_from.username, 'time': self.formatted_time, 'msg_to': self.msg_to.username,"m_f_id":self.msg_from.id}

    # def __unicode__(self):
    #     return '[{time}] {msg}: {msg_from}'.format(**self.as_dict())

    # def __str__(self):
    #     """String for representing the Model object."""
    #     return self.msg

