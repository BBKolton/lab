# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20160812_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='timestamp',
            field=models.CharField(max_length=16),
        ),
    ]
