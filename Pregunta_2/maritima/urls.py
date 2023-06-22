from django.urls import path
from .views import ListaConcesion, ejecutar_script

urlpatterns = [
    path('', ListaConcesion.as_view(), name='lista'), #muestra todos los registros obtenidos de la búsqueda
    path('guardar/', ejecutar_script, name='almacenar'), #se encarga de ejecutar el script que busca y almacena los datos en la DB
]