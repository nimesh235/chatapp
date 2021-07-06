from django.conf.urls import include, url
from django.urls import path,re_path
from django.views.generic import TemplateView
from . import consumer
from . import views


urlpatterns = [
    url(r"signup", views.signup),
    # url(r"send/", consumer.demo),
    path("chat/",views.home),
    re_path(r"chat/(?P<id>[-\w]+)/$", views.home),
    url(r'logout', views.logoutpage),
    url(r"login", views.loginpage)
]