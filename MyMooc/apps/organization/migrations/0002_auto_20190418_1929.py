# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-18 19:29
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='desc',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='机构描述'),
        ),
    ]
