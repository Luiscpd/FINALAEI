from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #path('select/', views.datos_huesped, name="select"),

]