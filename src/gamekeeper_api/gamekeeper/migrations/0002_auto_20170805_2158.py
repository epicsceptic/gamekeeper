# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-05 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamekeeper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='rules',
            field=models.ManyToManyField(blank=True, to='gamekeeper.Rule'),
        ),
        migrations.AlterField(
            model_name='event',
            name='rules',
            field=models.ManyToManyField(blank=True, to='gamekeeper.Rule'),
        ),
    ]