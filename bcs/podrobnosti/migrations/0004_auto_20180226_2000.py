# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-26 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podrobnosti', '0003_auto_20180226_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datoteka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stevilka', models.IntegerField(blank=True, null=True)),
                ('tekst', models.CharField(max_length=100)),
                ('datoteka', models.FileField(blank=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slika',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stevilka', models.IntegerField(blank=True, null=True)),
                ('tekst', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='dokumentacija',
            name='datoteka',
        ),
        migrations.RemoveField(
            model_name='dokumentacija',
            name='image',
        ),
        migrations.AddField(
            model_name='dokumentacija',
            name='datoteka',
            field=models.ManyToManyField(blank=True, to='podrobnosti.Datoteka'),
        ),
        migrations.AddField(
            model_name='dokumentacija',
            name='image',
            field=models.ManyToManyField(blank=True, to='podrobnosti.Slika'),
        ),
    ]
