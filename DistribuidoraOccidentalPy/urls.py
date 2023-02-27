
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('profile/<int:id>/', views.profile, name='profile'),

    path('login/',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('carro/', include('carrito.urls')),
    path('edit_profile/', views.UpdateUserView.as_view(), name="edit_user"),


]
