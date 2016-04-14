# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-13 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=20)),
                ('sku', models.CharField(max_length=60)),
                ('title', models.CharField(max_length=800)),
                ('brand', models.CharField(max_length=30)),
                ('seller', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('sku',),
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('five_star', models.IntegerField(default=0)),
                ('four_star', models.IntegerField(default=0)),
                ('three_star', models.IntegerField(default=0)),
                ('two_star', models.IntegerField(default=0)),
                ('one_star', models.IntegerField(default=0)),
            ],
        ),
    ]
