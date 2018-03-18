# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-18 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podrobnosti', '0002_auto_20180317_1726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='podrobnost',
            options={'ordering': ['specifikacija__stevilka']},
        ),
        migrations.AlterModelOptions(
            name='podskupina',
            options={},
        ),
        migrations.RemoveField(
            model_name='podskupina',
            name='specifikacija',
        ),
        migrations.AddField(
            model_name='podrobnost',
            name='specifikacija',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='podrobnosti.Specifikacija'),
        ),
    ]
