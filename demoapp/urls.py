from django.conf.urls import include, url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    # url('', views.index),
    # url('chat',views.chat),
    url(r"signup", views.signup),
    # url(r"demo/(?P<slug>[-\w]+)/$",views.demo),
    url(r"home/(?P<slug>[-\w]+)/send/$",views.send),
    # url("base",views.base),
    url(r"home/(?P<id>[-\w]+)/$", views.home),
    url(r'logout', views.logoutpage),
    url(r"login", views.loginpage)
]