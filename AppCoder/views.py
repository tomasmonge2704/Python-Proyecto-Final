from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiares,Curso,Post
from AppCoder.forms import CursoFormulario

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
def inicio(request):
    posts = Post.objects.all()
    return render(request,"home/index.html",{"posts":posts})
def cursoformulario(request):

    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            curso = Curso (nombre=informacion['curso'], camada=informacion['camada'])

            curso.save()

            return render(request, "home/index.html")
    else:
        miFormulario = CursoFormulario()

    return render(request, "home/index.html", {"miFormulario":miFormulario})

def busquedaCamada(request):
    return render(request,"home/busquedaCamada.html")
def buscar(request):
    respuesta = f"estoy buscando la camda nro: {request.GET['camada']}"
    return HttpResponse(respuesta)