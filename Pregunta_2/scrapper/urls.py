from django.urls import path
from .views import ListaJurisprudencia, DetalleJurisprudencia, almacenar_datos

urlpatterns = [
    path('', ListaJurisprudencia.as_view(), name='lista'), #muestra la lista de las jurisprudencias
    path('<int:pk>/', DetalleJurisprudencia.as_view(), name='detalle'), #muestra el detalle de cada jurisprudencia
    path('guardar/', almacenar_datos, name='almacenar'), #ejecuta la función que realiza el raspado web
]
