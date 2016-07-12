# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_adv_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adv',
            name='act_date',
            field=models.DateField(null=True, verbose_name='活动结束时间'),
        ),
        migrations.AlterField(
            model_name='adv',
            name='language',
            field=models.CharField(choices=[('en', '英文'), ('rs', '俄文'), ('fr', '法文'), ('gr', '德文')], default='en', max_length=500, verbose_name='语言'),
        ),
    ]