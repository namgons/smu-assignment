from django.contrib import admin
from contents import models as content_models


admin.site.register(content_models.Content)
