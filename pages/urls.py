#pages/urls.py
from django.urls import path
from .views import homePageView #el punto es para que vea en el actual directorio

urlpatterns = [
    path('', homePageView, name='home')
]
#cada url va a tener 3 partes
"""
    el primero es una regular expresion para la url
    el segundo es la funcion a la que llama la url 
    el tercero es un alias para hacer referencia en el template 
"""