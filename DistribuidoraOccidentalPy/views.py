from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import UserRegistroForm
from django.contrib.auth.models import User


def index(request):
    return render(request,'index.html',{      
})

def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user =User.objects.get(username=username)
    else:
        user =current_user
    return render(request,'editarprofile.html',{'user':user,})

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

def tienda(request):
    return render(request,'tienda.html',{      
})