# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-18 12:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrdep', '0004_auto_20160518_1046'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='staff',
            unique_together=set([('first_name', 'middle_name', 'last_name', 'birthday', 'post')]),
        ),
    ]
