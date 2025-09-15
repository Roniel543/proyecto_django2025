from django.shortcuts import render
from django.http import HttpResponse
from .models import TblCurso
from django.http import JsonResponse


# Create your views here.

def cursos(request):
    lista_cursos=TblCurso.objects.all()
    str_cursos = "<ul>\n"
    for curso in lista_cursos:
        str_cursos += f"<li>{curso.curso_titulo}</li>"
    str_cursos += "</ul>"
    return HttpResponse(f'<div style="text-align: center;"><h1>Mis Cursos Sphere</h1>{str_cursos}</div>')

#Aqui modificamos el header de la respuesta para que se descargue un archivo pdf
def holamundo(request):
    return HttpResponse("Hola mundo", headers={
        "Content-Type": "application/pdf",
        "Content-Disposition": 'attachment; filename="foo.pdf"',
    })


def cursos_api(request):
    lista_cursos = TblCurso.objects.all()

    lista_final = [
        {
            'id': curso.curso_id,
            'Titulo': curso.curso_titulo,
            'Descripcion_Prueba': curso.curso_descripcion,
        }
        for curso in lista_cursos
    ]
    
    dataJson = {
        'data' : lista_final
    }
    return JsonResponse(dataJson)

def mostrar_formulario(request):
    resultado = 0 
    if(request.method == 'POST'):
        n1 = int(request.POST['n1'])
        n2 = int(request.POST['n2'])
        resultado = n1 + n2
    return render(request,'formulario.html',{'resultado':resultado})

def mostrar_otroformulario(request):
    return render(request,'otro_formulario.html')