# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-03 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]