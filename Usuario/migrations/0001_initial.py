# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-29 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=45, unique=True)),
                ('nombre', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('ultima_conexion', models.DateTimeField(auto_now_add=True)),
                ('user_type', models.CharField(choices=[('Contador', 'Contador'), ('Admin', 'Admin'), ('Mesero', 'Mesero')], default='Admin', max_length=45)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
