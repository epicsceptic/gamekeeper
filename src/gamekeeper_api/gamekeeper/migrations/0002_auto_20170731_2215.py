# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-31 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamekeeper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rules',
            field=models.ManyToManyField(blank=True, to='gamekeeper.Rule'),
        ),
    ]
