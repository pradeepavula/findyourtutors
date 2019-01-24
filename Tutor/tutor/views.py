# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User

def TutorProfile(request):
    return render(request,"dashboard-tutor-profile-settings.html",locals())
def TutorSecurity(request):

    if request.method =="POST":
       userid = int(request.user.pk)
       password = request.POST.get('currentpassword',None) 
       new_password = request.POST.get('newpassword',None)
       confirm_password = request.POST.get('repassword',None)
       try:
           user_id = User.objects.get(id=userid)
           if user_id.check_password(password) != True:
               error ="invalid password the user"
               return render(request,"dashboard-tutor-security-settings.html",locals())
           else:
               if new_password == confirm_password:
                   user_id.set_password(new_password)
                   user_id.save()
               else:
                   error = "password mismatch"
                   return render(request,"dashboard-tutor-security-settings.html",locals())
       except Exception as e:
            error = e
            return render(request,"dashboard-tutor-security-settings.html",locals())
    return render(request,"dashboard-tutor-security-settings.html",locals())
