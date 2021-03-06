# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-14 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_reg', '0005_user'),
        ('hireme', '0005_auto_20180114_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=48)),
                ('info', models.CharField(max_length=240)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='login_reg.User')),
                ('saved_by', models.ManyToManyField(related_name='saved_by', to='login_reg.User')),
            ],
        ),
    ]
