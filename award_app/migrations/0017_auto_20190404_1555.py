# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-04 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award_app', '0016_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usability',
            field=models.CharField(max_length=2),
        ),
    ]