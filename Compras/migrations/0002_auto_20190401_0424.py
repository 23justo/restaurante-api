# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-01 04:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orden',
            old_name='no_mesa',
            new_name='numero_mesa',
        ),
    ]
