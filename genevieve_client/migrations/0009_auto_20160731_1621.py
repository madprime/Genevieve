# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 16:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genevieve_client', '0008_auto_20160628_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genomereport',
            old_name='report_type',
            new_name='report_source',
        ),
    ]