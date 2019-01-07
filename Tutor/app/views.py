# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.contrib.auth.models import User

from app.models import UserProfile
# Create your views here.

from django.http import HttpResponseRedirect,HttpResponse
from django.http import HttpResponse

def index(request):
    return render(request,"index.html",locals())

def signup(request):
    if request.method == "POST":
        joinas = request.POST.get('joinas',None)
        firstname = request.POST.get('firstname',None)
        lastname = request.POST.get('lastname',None)
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        user = User.objects.create_user(first_name=firstname,last_name=lastname,username = email,email= email,password = password)
        user.save()
        up = UserProfile()
        up.user = user
        up.user_type = joinas
        up.save()
        return render(request,"index.html",locals())
    else:
        return render(request,"index.html",locals())


def login(request):
    if request.method == "POST":
        username = request.POST.get('email', '')
        password = request.POST.get('password', '')
        print username, password
        from django.contrib import auth
        user = auth.authenticate(username=username,password=password)
        print user
        if user is not None and user.is_active:
           from django.contrib import auth
           auth.login(request, user)
           return HttpResponseRedirect("/profile/")
        else:
            e = "yes"
            return render(request,"index.html", locals())
            
    else:
        return render(request,"index.html", locals())
