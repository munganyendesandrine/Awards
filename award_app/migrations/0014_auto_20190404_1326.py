# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-04 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award_app', '0013_auto_20190404_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image_landing_page',
            field=models.ImageField(upload_to='picture/'),
        ),
    ]