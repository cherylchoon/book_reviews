# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 19:46
from __future__ import unicode_literals

import apps.login.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirm_password',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=55),
        ),
    ]
