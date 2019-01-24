from django.conf.urls import  include, url
from tutor.views import TutorProfile,TutorSecurity
urlpatterns = [
    url(r'^tutorprofile/$', TutorProfile),
    url(r'^tutorsecurity/$', TutorSecurity),

        ]


