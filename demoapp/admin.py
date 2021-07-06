from django.contrib import admin
from .models import Massage

# Register your models here.

# @admin.register(massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('msg', 'msg_from', 'msg_to','status', 'time')
    # pass

admin.site.register(Massage, MassageAdmin)
