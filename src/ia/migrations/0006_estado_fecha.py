# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0005_usuario_tz'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
