from django.apps import AppConfig

class GreetingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myproject1.greetings'  # Must match INSTALLED_APPS
