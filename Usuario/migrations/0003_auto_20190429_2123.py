# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-29 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_auto_20190429_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='compras_Inventario',
            new_name='facturacion_modulo',
        ),
        migrations.AddField(
            model_name='usuario',
            name='inventario_modulo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
