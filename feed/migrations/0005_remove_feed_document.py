# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-22 13:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_feed_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='document',
        ),
    ]
