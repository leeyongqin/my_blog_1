# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_body', models.TextField()),
            ],
        ),
    ]
