# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-01-21 14:26
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genevieve_client', '0010_auto_20160731_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='myvariant_gnomad_genome',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]
