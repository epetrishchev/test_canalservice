from django.apps import AppConfig


class GsbaseConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "gsbase"
    verbose_name: str = 'База заказов'
