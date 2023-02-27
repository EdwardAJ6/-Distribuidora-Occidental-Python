
from django.contrib import admin
from django.urls import include, path
from . import views

from django.conf.urls.static import static
from django.conf import settings 

from core.views import VistaListaProductos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('profile', views.profileSettings, name='profile'),
    path('login/',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('carro/', include('carrito.urls')),
    path('tienda/', VistaListaProductos.as_view(), name='tienda'),
    path('productos/', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)