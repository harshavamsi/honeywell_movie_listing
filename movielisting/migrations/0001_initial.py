# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_title', models.CharField(unique=True, max_length=200, blank=True)),
                ('director_name', models.CharField(max_length=200, blank=True)),
                ('actor_1_name', models.CharField(max_length=200, blank=True)),
                ('actor_2_name', models.CharField(max_length=200, blank=True)),
                ('genres', models.CharField(max_length=200, blank=True)),
                ('language', models.CharField(max_length=200, blank=True)),
                ('country', models.CharField(max_length=200, blank=True)),
                ('content_rating', models.CharField(max_length=200, blank=True)),
                ('budget', models.IntegerField(blank=True)),
                ('title_year', models.IntegerField(blank=True)),
                ('plot_keywords', models.CharField(max_length=200, blank=True)),
                ('movie_imdb_link', models.URLField(blank=True)),
            ],
        ),
    ]
