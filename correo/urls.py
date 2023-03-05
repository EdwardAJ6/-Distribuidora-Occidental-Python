from django.urls import path
from .views import enviar_correo


app_name = 'correo'

urlpatterns = [
    path('enviar/', enviar_correo, name='enviar_correo'),
]
