# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-01 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayit', '0007_example_audio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='song_name_1',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='musician',
            name='song_name_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='musician',
            name='song_url_1',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='musician',
            name='song_url_2',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='musician',
            name='profile_url',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]
