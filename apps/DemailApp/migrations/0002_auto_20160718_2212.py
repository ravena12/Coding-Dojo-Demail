# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DemailApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
