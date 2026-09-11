from django.shortcuts import render
from data import productos

def mostrar_productos(request):
    contexto = {
        'productos': productos
    }
    return render(request, 'catalogo/index.html', contexto)
