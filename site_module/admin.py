from django.contrib import admin
from . import models


class BackgroundColorAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class BackgroundImageAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


admin.site.register(models.SiteSettings)
admin.site.register(models.BackgroundColor, BackgroundColorAdmin)
admin.site.register(models.BackgroundImage, BackgroundImageAdmin)
