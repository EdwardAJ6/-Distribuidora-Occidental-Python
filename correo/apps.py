from django.apps import AppConfig

class CorreoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'correo'

    def ready(self):
        import correo.signals