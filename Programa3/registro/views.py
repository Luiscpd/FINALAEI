
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import CreateUser

# Create your views here.

def index(request):
    title = 'Formulario para registro de datos'
    return render(request, 'index.html', {
        'title': title
    })


def formulario(request):
    if request.method == 'POST':
        return render(request, 'formulario.html', {
            'form': CreateUser()
        })

    else:
        DatosUsuario.objects.create(DPI=request.POST["DPI"])
        DatosUsuario.objects.create(name=request.POST["name"])
        DatosUsuario.objects.create(lastname=request.POST["lastname"])
        DatosUsuario.objects.create(nickname=request.POST["nickname"])
        DatosUsuario.objects.create(email=request.POST["email"])
        DatosUsuario.objects.create(date=request.POST["date"])
        return redirect('index')

#def datos_huesped(request):
 #   if request.method == 'GET':
 #       return render(request, 'datos_huesped.html', {
 #           'form': CreateHuesped()
 #       })
 #   else:
 #       DatosHuesped.objects.create(DPI=request.POST["DPI"])
 #       DatosHuesped.objects.create(name=request.POST["name"])
 #       DatosHuesped.objects.create(lastname=request.POST["lastname"])
 #       DatosHuesped.objects.create(email=request.POST["email"])
 #       DatosHuesped.objects.create(habitacion=request.POST["habitacion"])
 #       return redirect('index')