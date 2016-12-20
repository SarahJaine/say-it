# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('product_type', models.CharField(max_length=100)),
                ('review', models.TextField(max_length=500, unique=True)),
                ('order', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='d', max_length=1)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Musicians',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('position', models.CharField(max_length=100)),
                ('musical_styles', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=500, unique=True)),
                ('profile_url', models.URLField(max_length=100)),
                ('order', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='d', max_length=1)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]