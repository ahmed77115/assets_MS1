from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MovementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "movement"
    verbose_name = _("الحركات")
    import movement.signals 


