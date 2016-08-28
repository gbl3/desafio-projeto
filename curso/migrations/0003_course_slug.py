# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, unique=True, verbose_name='Slug'),
        ),
    ]