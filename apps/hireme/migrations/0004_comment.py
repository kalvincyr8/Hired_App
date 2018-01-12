# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-10 05:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0003_user'),
        ('hireme', '0003_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('ratings', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_by', to='login_reg.User')),
                ('comment_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_on', to='hireme.Job')),
            ],
        ),
    ]