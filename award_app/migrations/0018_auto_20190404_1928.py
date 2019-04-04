# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-04 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award_app', '0017_auto_20190404_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='rating',
            name='content',
        ),
        migrations.AddField(
            model_name='rating',
            name='content',
            field=models.ManyToManyField(to='award_app.content'),
        ),
    ]
