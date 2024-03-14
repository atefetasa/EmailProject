from django.contrib import admin
from . import models

admin.site.register(models.Email)
admin.site.register(models.Label)
admin.site.register(models.ForwardedEmail)