from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #contex es un diccionario de variables que se pasan a la funcion desde el servidor
    context = {}
    return render(request, "web/index.html", context)
    