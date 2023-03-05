from django.shortcuts import render

from django.shortcuts import render
from django.core.mail import send_mail
from .models import CorreoMasivo
from usuario.models import User
from django.contrib import messages


def enviar_correo(request):
    if request.method == 'POST':
        asunto = request.POST.get('asunto')
        cuerpo = request.POST.get('cuerpo')

        correo = CorreoMasivo(asunto=asunto, cuerpo=cuerpo)
        correo.save()
        destinatarios = User.objects.all()
        correo.destinatarios.set(destinatarios)

        email_list = [user.email for user in destinatarios]

        send_mail(
            asunto,
            cuerpo,
            'ivanciclista2@gmail.com',
            email_list,
            fail_silently=False,
        )

        correo.enviado = True
        correo.save()
        messages.success(request, 'El correo masivo ha sido enviado correctamente.')

        return render(request, 'correos/enviar_correo.html')

    return render(request, 'correos/enviar_correo.html')
