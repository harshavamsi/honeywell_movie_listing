from django.conf.urls import url
# -*- coding: utf-8 -*-
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<movie_title>.*)/$', views.detail, name="detail" ),
]
