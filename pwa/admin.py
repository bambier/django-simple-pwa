from django.contrib import admin
from pwa.models import Permissions, ProgressiveWebApplication, Icons


@admin.register(Icons)
class IconAdmin(admin.ModelAdmin):
    list_display = ("name", "color_scheme", "purpose",)


@admin.register(Permissions)
class PermissionsAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ProgressiveWebApplication)
class PWAAdmin(admin.ModelAdmin):
    list_display = ("name", "scope", "start_url",)
