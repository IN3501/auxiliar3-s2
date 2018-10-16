from django.shortcuts import render

# Create your views here.
def index(request):
	contexto = {"saludo":"hola", "Cargo_1": "AuxiliaR", "Cargo_2": "Ayudante", "Cargo_3": "Profesor"}
	return render(request, 'app_de_IN3501/index.html',contexto)


def welcome(request):
	return render(request, 'app_de_IN3501/bienvenida.html')


def tarea(request):
	return render(request, 'app_de_IN3501/tarea.html')