from django.contrib.auth import authenticate, login, logout,user_logged_in
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import requires_csrf_token
import pusher

from .models import Massage


# Create your views here.

def loginpage(request):
    if request.method == "POST":
        print(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user)
            return redirect("/chat")
        else:
            print(request)
            # Return an 'invalid login' error message.
    else:
        return render(request, 'login.html', {'login': 'active'})


def signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["user_name"]
        e_mail = request.POST["e_mail"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 !=password2:
            return render(request, "signup.html", {'signup': 'active'})
        else:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=e_mail,password=password1)
            user.save()
            return redirect("/home/login")
    else:
        return render(request, "signup.html", {'signup': 'active'})


def logoutpage(request):
    logout(request)
    return redirect("/login")


@login_required(login_url='/login')
def home(request, id="New", **kwargs):

    print(id)
    users = User.objects.filter(~Q(id=request.user.id))
    if id != "New":
        msg_from = User.objects.filter(id=request.user.id)
        user = User.objects.get(id=id)
        # print(msg_from)
        m = Massage.objects.filter(
            (Q(msg_from=msg_from[0]) & Q(msg_to=user)) | Q(msg_to=msg_from[0]) & Q(msg_from=user))

        return render(request, "home.html",
                      {"home": "active", "users": users, "id": int(id), "user": user, "datas": m,"cuser":request.user})
    else:
        return render(request, "home.html", {"home": "active", "users": users})


def send(request, slug):
    if request.POST["msg"]:
        msg = request.POST["msg"]
        msg_from = User.objects.get(id=request.user.id)
        msg_to = User.objects.get(id=slug)
        m = Massage(msg=msg, msg_from=msg_from, msg_to=msg_to)
        m.save()

    return redirect(f'/home/{slug}/')

