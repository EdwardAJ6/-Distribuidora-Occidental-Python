from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from DistribuidoraOccidentalPy import settings

class Correo(models.Model):
    asunto = models.CharField(max_length=100)
    destinatario = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.asunto

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