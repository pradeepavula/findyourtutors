# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-19 08:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_historicalprofile_historicaluserprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalUserProfile',
            new_name='HistoricalUserType',
        ),
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='UserType',
        ),
        migrations.AlterModelOptions(
            name='historicalusertype',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical user type'},
        ),
    ]
