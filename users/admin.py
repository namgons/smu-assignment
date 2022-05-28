from django.contrib import admin
from . import models as user_models

admin.site.register(user_models.User)
