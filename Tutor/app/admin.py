# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from app.models import *
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(UserProfile,SimpleHistoryAdmin)
admin.site.register(Profile,SimpleHistoryAdmin)
