from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto
from .forms import productoform
# Create your views here.
#metodo que devuelve en json
def lista_productos(request):
    #obtener todas las intancias del objetode la DB
    productos = Producto.objects.all()
    
    #contruir una variable en fomrto diccionario
    #pq el json response , lo requiere
    data = [
        {
            #objeto de roducto a l wey
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]
    
    #devolve la respuest json
    return JsonResponse(data, safe=False)

#funcion para mandar a la vista del form

def agregar_producto(request):
    #averiguar si estamos teniendo una respuesta al formulario
    if request.method == 'POST':
        form = productoform(request.POST)
        if form.is_valid():
            form.save()
            print('guardado')
            return redirect('lista') #redirige a la vista ver
    else:
        form = productoform()
    return render(request, 'agregar.html',{'form':form})

        
    # pintar un formulario vacio
    
 