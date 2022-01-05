from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Users'

    # Ready method : https://docs.djangoproject.com/en/4.0/ref/applications/#django.apps.AppConfig.ready
    def ready(self):
        import Users.signals