from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DirrecionesEnvios
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .forms import DireccionesForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from orden.utils import crear_obtener_orden
from carrito.utils import crear_obtener_carrito

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

    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().user_id:
            return redirect('carrito:carro')

        return super(DireccionesEnvioUpdate, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('direcciones:direcciones', kwargs={
            #'pk': self.object.pk
        })



@login_required(login_url='login')
def create(request):
    form = DireccionesForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        direcciones = form.save(commit=False)
        direcciones.user = request.user
        direcciones.default = not  DirrecionesEnvios.objects.filter(user=request.user).exists()

        direcciones.save()

        if request.GET.get('next'):
            if request.GET['next'] == reverse('orden:direccion'):
                carrito= crear_obtener_carrito(request)
                orden = crear_obtener_orden(carrito,request)

                orden.update_shipping_direccion(direcciones)
                return HttpResponseRedirect(request.GET['next'])

        messages.success(request, 'Direccion creada exitosamente')
        return redirect('direcciones:direcciones')

    return render(request,'direcciones/agregarDireccion.html', {
        'form': form
    })

@login_required(login_url='login')
def default(request, pk):
    direcciones = get_object_or_404(DirrecionesEnvios, pk=pk)

    if request.user.id != direcciones.user_id:
        return redirect('carrito:carro')
    DirrecionesEnvios.set_default_false(request.user)
    direcciones.set_default()

    messages.success(request, 'Dirección principal actualizada')

    return redirect('direcciones:direcciones')