# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-09 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_type',
            field=models.IntegerField(choices=[(1, '课程'), (2, '课程机构'), (3, '讲师')], default=1, max_length=1, verbose_name='收藏类型'),
        ),
    ]