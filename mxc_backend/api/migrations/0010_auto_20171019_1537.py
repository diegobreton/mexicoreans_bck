# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 22:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20171019_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='levelCollection',
            new_name='lessonCollection',
        ),
    ]
