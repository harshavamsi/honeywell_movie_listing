from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(blank=True,max_length=200)
    director_name = models.CharField(blank=True,max_length=200)
    actor_1_name = models.CharField(blank=True,max_length=200)
    actor_2_name = models.CharField(blank=True,max_length=200)
    genres = models.CharField(blank=True,max_length=200)
    language = models.CharField(blank=True,max_length=200)
    country = models.CharField(blank=True,max_length=200)
    content_rating = models.CharField(blank=True,max_length=200)
    budget = models.CharField(blank=True,max_length=200)
    title_year = models.CharField(blank=True,max_length=200)
    plot_keywords = models.CharField(blank=True,max_length=200)
    movie_imdb_link = models.URLField(blank=True)

    def __unicode__(self):
        return self.movie_title
