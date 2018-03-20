# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('podrobnosti', '0001_initial'),
        ('popisi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='predmetmerila',
            name='dela',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='popisi.Dela'),
        ),
        migrations.AddField(
            model_name='podrobnost',
            name='merilo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='podrobnosti.Merilo'),
        ),
        migrations.AddField(
            model_name='podlagamerila',
            name='dokumentacija',
            field=models.ManyToManyField(blank=True, to='podrobnosti.Dokumentacija'),
        ),
        migrations.AddField(
            model_name='podlagamerila',
            name='predmet_merila',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='podrobnosti.PredmetMerila'),
        ),
        migrations.AddField(
            model_name='podlagamerila',
            name='slika',
            field=models.ManyToManyField(blank=True, to='podrobnosti.Slika'),
        ),
        migrations.AddField(
            model_name='merilo',
            name='podlaga_merila',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='podrobnosti.PodlagaMerila'),
        ),
    ]