from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Correo
from DistribuidoraOccidentalPy import settings

@receiver(post_save, sender=Correo)
def enviar_correo(sender, instance, created, **kwargs):
    if created:
        asunto = instance.asunto
        destinatario = instance.destinatario
        mensaje = instance.mensaje
        send_mail(
            asunto,
            mensaje,
            settings.EMAIL_HOST_USER,
            [destinatario],
            fail_silently=False,
        )


