from django.apps import AppConfig


class ShortenerConfig(AppConfig):
    """
    Configuration class for the Shortener app.

    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shortener'
