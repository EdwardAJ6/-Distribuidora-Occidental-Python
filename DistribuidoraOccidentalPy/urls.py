
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('ola', views.ola, name='ola'),
    path('login/',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('carro/', include('carrito.urls'))

]
