# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-14 23:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hireme', '0005_auto_20180114_2343'),
        ('login_reg', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]