# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_auto_20160813_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='FUCKDJANGO',
            field=models.CharField(default='fuck django', max_length=1337),
            preserve_default=False,
        ),
    ]
