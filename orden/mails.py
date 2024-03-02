from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.urls import reverse

class Mail:
    
    ##Codigo para urls en desarrollo (cambiar)
    @staticmethod
    def obtener_url_compras(url):
        if settings.DEBUG:
            return 'https://disoccidentalpy.azurewebsites.net{}'.format(
                reverse(url)
            )
    
    @staticmethod
    def enviar_orden_completada(orden, usuario):
        subject = 'Tu pedido ha sido enviado'
        template = get_template('ordenes/mails/completado.html')
        content = template.render({
            'usuario' : usuario,
            'next_url' : Mail.obtener_url_compras('orden:completadas')
        })
        
        message = EmailMultiAlternatives(subject, 
                                         'Mensaje importante',
                                         settings.EMAIL_HOST_USER,
                                         [usuario.email])
        
        message.attach_alternative(content, 'text/html')
        message.send()