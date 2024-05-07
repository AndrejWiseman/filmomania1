from django.apps import AppConfig


class TaggedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tagged'
