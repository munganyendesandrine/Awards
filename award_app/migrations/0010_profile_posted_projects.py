# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award_app', '0009_auto_20190403_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='posted_projects',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]