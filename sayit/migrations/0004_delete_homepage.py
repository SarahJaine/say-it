# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 22:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sayit', '0003_homepage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HomePage',
        ),
    ]