# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-20 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podrobnosti', '0007_auto_20180319_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='podrobnost',
            name='komentar',
            field=models.TextField(blank=True),
        ),
    ]