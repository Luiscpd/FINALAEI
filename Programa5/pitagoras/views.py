from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import *

# Create your views here.

def index(request):
    title = 'Bienvenido al cálculo de la hipotenusa'
    return render(request, 'index.html', {
        'title': title
    })