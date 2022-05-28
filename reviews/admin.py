from django.contrib import admin
from . import models as review_models

admin.site.register(review_models.Review)
