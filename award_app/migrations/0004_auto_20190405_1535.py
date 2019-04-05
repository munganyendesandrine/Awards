# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-05 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('award_app', '0003_auto_20190405_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating2',
            old_name='content_like',
            new_name='content_rate',
        ),
        migrations.RenameField(
            model_name='rating2',
            old_name='design_like',
            new_name='design_rate',
        ),
        migrations.RenameField(
            model_name='rating2',
            old_name='usability_like',
            new_name='usability_rate',
        ),
        migrations.RemoveField(
            model_name='rating2',
            name='content_unlike',
        ),
        migrations.RemoveField(
            model_name='rating2',
            name='design_unlike',
        ),
        migrations.RemoveField(
            model_name='rating2',
            name='usability_unlike',
        ),
    ]