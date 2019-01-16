# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords



class UserProfile(models.Model):
    user_type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    history = HistoricalRecords()
    def __str__(self):
        return self.user_type
class Profile(models.Model):
    user_type = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    history = HistoricalRecords()
    def __str__(self):
        return self.user_type
