# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-22 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0009_promocion_promocionproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocion',
            name='activa',
            field=models.BooleanField(default=True),
        ),
    ]