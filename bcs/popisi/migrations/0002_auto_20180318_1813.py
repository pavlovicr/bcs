# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-18 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popisi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dela',
            name='tekst',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='popisnapostavka',
            name='tekst',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='postavka',
            name='tekst',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='vrstadel',
            name='tekst',
            field=models.CharField(max_length=500),
        ),
    ]