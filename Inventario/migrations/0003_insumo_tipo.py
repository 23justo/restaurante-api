# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-01 02:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0002_insumotipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='insumo',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Inventario.InsumoTipo'),
            preserve_default=False,
        ),
    ]
