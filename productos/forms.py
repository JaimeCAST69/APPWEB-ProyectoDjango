#vamos ac rec modelos
from .models import Producto
from django import forms

#crear clase por cad formulario 

class productoform(forms.ModelForm):
    #defdinir los metadatso en la clase meta
    class Meta:
        #personalizar
        model = Producto
        # definir los campos de aparicion
        fields = ['nombre', 'precio','imagen']
        
        #atributos
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder':'ingresa el nombre'
                }
            )
        }
        
        #personalizar las etiquetas o textos que sale alado de los inputs
        labels = {
            'nombre': 'Nombre del producto',
            'precio' : 'Precio (MXN)',
            'imagen' : 'url de la imagen'
        }
        
        #personalizar lo msj de error
        error_messages ={
            'precio' : {
                'required':'El precio no debe estar vacío',
                'invalid':'Ingresa un valor valido'
            }
        }