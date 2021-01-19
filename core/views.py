from django.shortcuts import render, HttpResponse

html_cabecera = """
    <h1>Welcome</h1>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/presentacion/">Presentación</a></li>
        <li><a href="/contacto">Contacto</a></li>
        <li><a href="/catalogo">Catálogo</a></li>
    </ul>
"""

# Create your views here.


def home(request):
    return HttpResponse(html_cabecera + "<h1>Mi primera Vista en Django</h1>")


def presentacion(request):
    return HttpResponse(html_cabecera + "<h1>Hola Soy Christian</h1>")


def contacto(request):
    return HttpResponse(html_cabecera + "<h1>Mi número es 099999999</h1>")


def catalogo(request):
    return HttpResponse(html_cabecera + "<h1>Estudio de 4to Nivel</h1>")
