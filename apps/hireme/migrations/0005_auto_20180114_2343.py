# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-14 23:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hireme', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_by',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_on',
        ),
        migrations.RemoveField(
            model_name='job',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='job',
            name='saved_by',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
