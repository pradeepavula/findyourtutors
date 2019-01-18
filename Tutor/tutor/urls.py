from django.conf.urls import  include, url
from tutor.views import TutorProfile
urlpatterns = [
    url(r'^tutorprofile/$', TutorProfile),

        ]


