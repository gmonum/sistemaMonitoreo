# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-07 02:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaMonitoreo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name': 'un empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelOptions(
            name='multimedia',
            options={'verbose_name': 'un documento', 'verbose_name_plural': 'documentos'},
        ),
    ]