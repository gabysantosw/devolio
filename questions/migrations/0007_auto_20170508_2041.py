# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20170507_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Question title'),
        ),
    ]
