from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import UserRegistroForm
from core.models import Producto
from usuario.models import User
#Modelo PQRS
from core.models import Pqr
from .forms import UserRegistroForm,UsuarioActualizar,EditUserProfileForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from core.forms import PqrForm
from django.contrib import messages
from datetime import datetime, timedelta

def tienda(request):

    productos = Producto.objects.all().order_by('-id')

    return render(request,'tienda/tienda.html',{    
        'message': 'Lista Productos',
        'title': 'Productos',
        'productos': productos,
})

def index(request):
    return render(request,'index.html',{      
})

def profile(request, id):
    current_user = request.user
    if id and id != current_user.id:
        user =User.objects.get(pk=id)
    else:
        user =current_user
    return render(request,'cuenta/profile.html',{'user':user,})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            if user.is_staff:
                return redirect('admin:index')
            else:
                return redirect('index')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'cuenta/login.html',{})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')

def registro(request):
    data = {
        'form': UserRegistroForm()
    }

    if request.method == 'POST':
        formulario = UserRegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            messages.success(request,'Usuario ha sido creado' )
            return redirect('login')
        data["form"] = formulario 
    return render(request, 'cuenta/registro.html',data)

def tienda(request):
    return render(request,'tienda/tienda.html',{      
})

class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    form_class = EditUserProfileForm
    login_url = 'login'
    template_name = "cuenta/editarprofile.html"
    success_url = reverse_lazy('index')
    success_message = "User updated"

    def get_object(slef):
        return slef.request.user

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             "Please submit the form carefully")
        return redirect('index')

def ordenar(request):
    return render(request,'ordenes/ordenar.html',{      
})

@login_required(login_url='login')
def ver_pqrs(request):
    pqrs = Pqr.objects.filter(usuario=request.user).order_by('id')
    estimated_response_date = datetime.now() + timedelta(days=3)
    context = { 
        'estimated_response_date': estimated_response_date,
        'pqrs': pqrs,
    }
    return render(request,'cuenta/pqrs.html',context)


@login_required(login_url='login')
def añadir_pqrs(request):

        url = request.META.get('HTTP_REFERER')
        if request.method == 'POST':
            form = PqrForm(request.POST)
            if form.is_valid():
                data = form.save(commit=False)
                data.ip = request.META.get('REMOTE_ADDR')
                data.usuario_id = request.user.id  # asignar el id del usuario en la columna "usuario_id"
                data.save()
                messages.success(request, 'Gracias! Tu opinión ha sido enviada.')
                return redirect(url)
            else:
                print(form.errors)
        # crear una respuesta si la solicitud no es del tipo POST o el formulario no es válido
        return HttpResponse("La solicitud no es válida")


