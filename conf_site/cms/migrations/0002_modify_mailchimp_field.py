# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-19 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='mailchimp_url',
        ),
        migrations.AddField(
            model_name='homepage',
            name='mailchimp_list_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
