# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='test@email.com', max_length=100),
            preserve_default=False,
        ),
    ]
