from django.urls import path
from .views import *

urlpatterns = [
    path('api/get/', card_categorias, name='lista'),
    path('registrar/', agregar_categoria, name='agregar'),
    path('json/', lista_categoria, name='json'),
]
