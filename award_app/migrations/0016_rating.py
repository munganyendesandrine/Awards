# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-04 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award_app', '0015_auto_20190404_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.CharField(max_length=20)),
                ('usability', models.ImageField(null=True, upload_to='picture/')),
                ('content', models.CharField(max_length=60)),
            ],
        ),
    ]