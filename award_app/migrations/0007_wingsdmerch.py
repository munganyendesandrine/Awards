# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award_app', '0006_projects_link_to_livesite'),
    ]

    operations = [
        migrations.CreateModel(
            name='wingsdMerch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]