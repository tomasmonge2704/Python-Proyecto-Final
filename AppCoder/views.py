from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiares
# Create your views here.
def saludar(request):
	return HttpResponse("hola mundo")
def saludar_a(request, nombre):
	return HttpResponse(f"hola {nombre.capitalize()}")
def mostrar_mi_template(request):
    context = {     
        "Familiares": Familiares.objects.all(),
    }
    return render(request,"home/index.html", context)
