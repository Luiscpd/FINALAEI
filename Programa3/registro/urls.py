from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('formulario/', views.DatosUsuario, name="formulario")
 #   path('', views.cantidad_huespedes, name="cantidad_huespedes"),
 #   path('', views.selecionar_fecha, name="selecionar_fecha"),
 #   path('', views.precio, name="precio")    
]