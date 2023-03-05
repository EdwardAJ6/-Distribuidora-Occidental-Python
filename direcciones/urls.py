from django.urls import path
from . import views

app_name = 'direcciones'

urlpatterns = [

    path('',views.DireccionesEnvioView.as_view(),name='direcciones'),
    path('nuevo',views.create,name='create'),
    path('editar/<int:pk>',views.DireccionesEnvioUpdate.as_view(),name='update'),
    path('default/<int:pk>',views.default,name='default'),



]
