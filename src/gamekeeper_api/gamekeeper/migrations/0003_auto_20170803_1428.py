# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamekeeper', '0002_auto_20170802_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rule',
            name='action',
        ),
        migrations.AddField(
            model_name='rule',
            name='triggered_action',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='triggering_rules', to='gamekeeper.Action'),
        ),
        migrations.AddField(
            model_name='rule',
            name='triggering_action',
            field=models.ForeignKey(default=-2017, on_delete=django.db.models.deletion.CASCADE, related_name='triggered_rules', to='gamekeeper.Action'),
            preserve_default=False,
        ),
    ]
