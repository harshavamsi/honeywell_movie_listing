# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movielisting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title_year',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
