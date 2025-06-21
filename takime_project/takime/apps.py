from django.apps import AppConfig
from django.core.cache import cache

class TakimeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'takime'

    def ready(self):
        cache.clear()
        print("✔ Cache cleared on startup.")