# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-20 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koyla', '0002_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='flip',
            field=models.BooleanField(),
        ),
    ]