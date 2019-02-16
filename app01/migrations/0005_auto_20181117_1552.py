# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-11-17 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20181117_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='uid',
            field=models.CharField(default=2, help_text='微信用户绑定和CC视频统计', max_length=64, unique=True),
            preserve_default=False,
        ),
    ]