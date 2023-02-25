from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import UserRegistroForm
from core.models import Producto
from usuario.models import User

def tienda(request):

    productos = Producto.objects.all().order_by('-id')

    return render(request,'tienda.html',{    
        'message': 'Lista Productos',
        'title': 'Productos',
        'productos': productos,
})

def index(request):
    return render(request,'index.html',{      
})

def ola(request):
    return render(request,'ola.html',{      
})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('admin:index')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html',{})

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
    return render(request, 'registro.html',data)

