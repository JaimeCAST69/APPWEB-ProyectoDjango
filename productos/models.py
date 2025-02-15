from django.db import models

# Create your models here.
class Producto(models.Model):
    #atributos
    nombre = models.CharField(max_length=100) #mandar a contruir un campo
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    
    def __str__(self):
        return self.nombre
      