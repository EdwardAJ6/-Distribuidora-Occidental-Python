from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DirrecionesEnvios
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .forms import DireccionesForm
from django.contrib.messages.views import SuccessMessageMixin

class DireccionesEnvioView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = DirrecionesEnvios
    template_name = 'direcciones/dirreccionesEnvio.html'

    def get_queryset(self):
        return DirrecionesEnvios.objects.filter(user=self.request.user).order_by('-default')
    
class DireccionesEnvioUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = 'login'
    model = DirrecionesEnvios
    form_class = DireccionesForm
    template_name = 'direcciones/update.html'
    success_message = 'Direccion actualizada'

    def get_success_url(self):
        return reverse('direcciones:direcciones')
    


@login_required(login_url='login')
def create(request):
    form = DireccionesForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        direcciones = form.save(commit=False)
        direcciones.user = request.user
        direcciones.default = not  DirrecionesEnvios.objects.filter(user=request.user).exists()

        direcciones.save()

        messages.success(request, 'Direccion creada exitosamente')
        return redirect('direcciones:direcciones')

    return render(request,'direcciones/agregarDireccion.html', {
        'form': form
    })