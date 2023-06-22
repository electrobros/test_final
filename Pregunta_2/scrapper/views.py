from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import Jurisprudencia, Valores
import requests
import json

# Create your views here.
#Vista basada en clase, heredada de ListView con el propósito de simplificar el código
class ListaJurisprudencia(ListView):
    model = Jurisprudencia
    template_name = 'scrapper_list.html'

#Vista basada en clase, heredada de DetailView con el propósito de simplificar el código
class DetalleJurisprudencia(DetailView):
    model = Jurisprudencia
    template_name = 'scrapper_detail.html'

#función que al ejecutarse, realiza el raspado web
def almacenar_datos(request):
    #configuración del User-agent para evitar posibles bloqueos de la api
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'}
    # Url de donde se extrae la petición POST
    url = 'https://www.buscadorambiental.cl/buscador-api/jurisprudencias/list'
    #datos para el request en formato JSON
    consulta = request.POST['busqueda'] #variable que se recibe de la búsqueda de jurisprudencia que hará el usuario, en este caso se limita la búsqueda
    data = {"orden": "nuevo", "page":1, "pageSize":1000, "search": consulta}#payload detectado de la peticion POST
    response = requests.post(url, json=data, headers=headers)
    #objeto en formato JSON, de este se obtiene la jurisprudencia y los valores de la misma
    datos = json.loads(response.text)

    for jurisprudencia in datos['jurisprudencias']:
        #almacenamiento de la jurisprudencia
        modeloJurisprudencia = Jurisprudencia.objects.create( id_jurisprudencia = jurisprudencia['id'],
                                                        tipoCausa = jurisprudencia['tipoCausa'],
                                                        rol = jurisprudencia['rol'],
                                                        caratula = jurisprudencia['caratula'],
                                                        nombreProyecto = jurisprudencia['nombreProyecto'],
                                                        fechaSentencia = jurisprudencia['fechaSentencia'],
                                                        descriptores = jurisprudencia['descriptores'],
                                                        linkSentencia = jurisprudencia['linkSentencia'],
                                                        urlSentencia = jurisprudencia['urlSentencia'],
                                                        activo = jurisprudencia['activo'],
                                                        tribunal = jurisprudencia['tribunal'],
                                                        tipo = jurisprudencia['tipo'],
                                                        relacionada = jurisprudencia['relacionada'],
                                                        visitas =jurisprudencia['visitas'])
        
        modeloJurisprudencia.save()
        
        for valor in jurisprudencia['valores']:
            modeloValores = Valores.objects.create(id_valor = valor['id'],
                                                idParametro = valor['idParametro'],
                                                idItemlista = valor['idItemlista'],
                                                valor = valor['valor'],
                                                parametro = valor['parametro'],
                                                item = valor['item'],
                                                idjurisprudencia = modeloJurisprudencia)
            modeloValores.save()
    return redirect('lista')

