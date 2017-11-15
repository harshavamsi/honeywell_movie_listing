# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movielisting', '0002_auto_20171115_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_title',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
