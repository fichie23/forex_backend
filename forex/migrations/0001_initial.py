# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-22 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.CharField(max_length=3, unique=True)),
                ('target', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRateHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rate', models.FloatField(default=1.0)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forex.Currency', unique_for_date=True)),
            ],
        ),
    ]