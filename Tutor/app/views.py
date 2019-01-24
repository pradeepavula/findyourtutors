# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.contrib.auth.models import User

from app.models import UserType
# Create your views here.

from django.http import HttpResponseRedirect,HttpResponse
from django.http import HttpResponse
from serializers import UserSerializer

from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.contrib.auth.models import User
def index(request):
    return render(request,"index.html",locals())

"""
def validation(request):
    email = request.get("email")
    if email == "":
"""     
def signup(request):
    if request.method == "POST":
        joinas = request.POST.get('joinas',None)
        firstname = request.POST.get('firstname',None)
        lastname = request.POST.get('lastname',None)
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        username = email
        try:
            #user = User.objects.create_user(first_name=firstname,last_name=lastname,username = email,email= email,password = password)
            #user.save()
            params ={"first_name":firstname,"last_name":lastname,"email":email,"username":email,"password":password}
            ser = UserSerializer(data = params)
            if ser.is_valid():
                ser.save()
                #user_obj = User.objects.get(email=
                up = UserProfile()
                up.user= ser.instance
                up.user_type = joinas
                up.save()
                success = "yes"
                return render(request,"index.html",locals())
            else:
                e = ser.errors
                
                return render(request,"index.html",locals())
        except Exception as err:
            e= err
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
           auth.login(request, user)
           userid = int(user.id)
           try:
               up =  UserType.objects.get(user_id = userid)
               if up.user_type == "tutor":
                   return render(request,"dashboard-tutor.html",locals())
           except :
               return render(request,"index.html", locals())
        else:
            e = "yes"
            return render(request,"index.html", locals())
            
    else:
        return render(request,"index.html", locals())

def preprocess_email_body(request, url='url'):
    return ''

def forgotpwd(request):
    if request.method=="POST":
        email=request.POST.get('email')
        uemail = User.objects.filter(email = email)
        try:
            uid = uemail[0].id
            subject="Reset Password"
            url='http://127.0.0.1:8000/resetpwd/{0}'.format(uid)
            html_content='<a href="%s" > click here</a>'% url
            body = preprocess_email_body(request,  html_content)
            email =EmailMultiAlternatives(subject,body,to=[email])
            content_subtype = "html"
            email.attach_alternative(html_content, "text/html")
            email.send()
            success = "yes"
        except Exception as e:
            e ="yes"
            return render (request,"forgotpwd.html",locals())
    return render (request,"forgotpwd.html",locals())
def resetpwd(request,uid):
    if request.method=="POST":
        pwd=request.POST.get('password')
        user = User.objects.get(id=uid)
        user.set_password(pwd)
        user.save()
        success ="yes"
        return render(request,"resetpwd.html",locals())
    return render(request,"resetpwd.html",locals())
