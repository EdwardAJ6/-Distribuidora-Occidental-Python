from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import UserRegistroForm,UsuarioActualizar
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    return render(request,'index.html',{      
})

def profile(request, id):
    current_user = request.user
    if id and id != current_user.id:
        user =User.objects.get(pk=id)
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

def actualizar_registro(request, pk):
    registro = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        registro.first_name = request.POST['first_name']
        registro.save()
        return redirect('index', pk=registro.pk)
    else:
        return render(request, 'index.html', {'registro': registro})