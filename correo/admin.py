from django.contrib import admin
from .models import Correo

class CorreoAdmin(admin.ModelAdmin):
    list_display = ('asunto', 'destinatario', 'mensaje')

    
admin.site.register(Correo, CorreoAdmin)
