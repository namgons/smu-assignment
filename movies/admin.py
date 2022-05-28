from django.contrib import admin
from . import models as movie_models

admin.site.register(movie_models.Movie)
