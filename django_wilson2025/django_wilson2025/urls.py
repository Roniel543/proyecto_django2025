"""
URL configuration for django_wilson2025 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from courses.views import cursos, holamundo,cursos_api, mostrar_formulario,mostrar_otroformulario

def saludo(request):
    nombre = request.GET['nombre']
    return HttpResponse(f'<center>Hola {nombre}</center>')

def suma(request,n1,n2):
    resultado = n1 + n2
    return HttpResponse('El resultado de la suma es: '+ str(resultado) )

def calculadora(request):
    n1 = int(request.GET.get('n1'))
    n2 = int(request.GET.get('n2'))
    operacion = request.GET.get('operacion')
    if(operacion == 'suma'):
        resultado = n1 + n2
    elif(operacion == 'resta'):
        resultado = n1 - n2
    elif(operacion == 'multiplicacion'):
        resultado = n1 * n2
    elif(operacion == 'division'):
        if(n2 == 0):
            resultado = "Error: No se puede dividir por 0"
        else:
            resultado = n1 / n2
    return HttpResponse(f'El resultado de la {operacion} es: {resultado}')


def convertir(request):
    valor = int(request.GET.get('valor'))
    unidad=request.GET.get('unidad')
    if(unidad == 'celsius'):
        resultado = (valor * 9/5) + 32
        unidad = "fahrenheit"
    elif(unidad == 'fahrenheit'):
        resultado = (valor - 32) * 5/9
        unidad = "celsius"
    else:
        resultado = "Unidad en desarrollo"
    return HttpResponse("El valor de la conversion es: " + str(resultado) + " " + unidad)

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('holamundo/',holamundo),
    path('cursos/', cursos), 
    path('cursos/api/',cursos_api),
    path('suma/<int:n1>/<int:n2>',suma),
    path("calculadora/", calculadora),
    path("convertir/", convertir),
    path("formulario/", mostrar_formulario),
    path("formulario2/", mostrar_otroformulario),
]
