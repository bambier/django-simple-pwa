from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PwaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pwa'
    verbose_name = _("PWA")
