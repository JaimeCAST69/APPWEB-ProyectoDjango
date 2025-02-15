
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Categoria
from .forms import CategoriaForm

def lista_categoria(request):
    categorias = Categoria.objects.all()
    data = [
        {
        'nombre': c.nombre,
        'imagen': c.imagen
        }
        for c in categorias
    ]
    return JsonResponse(data, safe=False)

def card_categorias(request):
    return render(request, 'cards_categorias.html')

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = CategoriaForm()
    return render(request, 'registrar.html', {'form': form})
