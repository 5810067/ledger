# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='cost_value',
            field=models.CharField(max_length=200),
        ),
    ]
