
from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views


from django.conf.urls.static import static
from django.conf import settings 

from core.views import VistaListaProductos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('profile/<int:id>/', views.profile, name='profile'),

    path('login/',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('ordenar/', views.ordenar, name='ordenar'),
    path('carro/', include('carrito.urls')),
    path('carro/',views.login_view, name='carro'),
    path('tienda/', VistaListaProductos.as_view(), name='tienda'),
    path('productos/', include('core.urls')),
    path('edit_profile/', views.UpdateUserView.as_view(), name="edit_user"),
    # ruta PQRS 
    path('PQRS/',views.ver_pqrs, name='pqrs'),
    path('subir_pqr/',views.añadir_pqrs, name='subir_pqr'),
    path('direcciones/', include('direcciones.urls')),
    path('orden/', include('orden.urls')),
    path('inventario/', include('inventario.urls')),
    path('correo/', include('correo.urls')),
    path('buscar/', views.buscar_productos, name='buscar'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('reset_password_complete/', auth_views.PasswordChangeDoneView.as_view(), name='password_reset_complete'),
    path('accounts/login/',views.login_view, name='accounts_login'),









]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)