#modulos de selenium para realizar el raspado de la web
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import json
#modulos para el manejo de vistas
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Concesion

# Create your views here.
#clase que hereda de ListView, esta muestra los valores de las concesiones
class ListaConcesion(ListView):
    model = Concesion
    template_name = 'maritima_list.html'

#funcion para ejecutar el script de selenium
def ejecutar_script(request):
    driver = webdriver.Edge() #crea una instancia del driver del navegador
    # Abrir una página web con el driver de Microsoft Edge
    driver.get('https://www.concesionesmaritimas.cl/')
    wait = WebDriverWait(driver, 20, 0.5) #esperamos mientras carga la pagina

    #busqueda del frame central 
    driver.switch_to.frame('centro_sigmar')#cambio de contexto al frame central

    #localización del iframe donde se encuentra la tabla con los datos
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)#cambio al contexto del 
    
    #selección de filtros
    #filtro de la region
    region = Select(driver.find_element(By.NAME,'variableRegion'))
    region.select_by_value('2')#se escoge el valor de la lista (esto podría hacerse de forma dinámica a través de un formulario)
    #filtro de la gobernacion
    gobernacion = Select(driver.find_element(By.NAME,'variableGobmar'))
    gobernacion.select_by_value('12') #se escoge el valor de la lista (esto podría hacerse de forma dinámica a través de un formulario)
    #filtro de la capitania
    capitania = Select(driver.find_element(By.NAME, 'variableCapuerto'))
    capitania.select_by_value('13')#se escoge el valor de la lista (esto podría hacerse de forma dinámica a través de un formulario)
    #seleccion de boton
    boton = driver.find_element(By.NAME,'verlistado')
    boton.click()#se hace click para desplegar la búsqueda

    #A continuación, se adjunta, el guardado de la búsqueda, recorrido de la paginación y la generación del archivo JSON
    tabla_recorrido = driver.find_element(By.XPATH, '/html/body/font/form/p[4]/font/table')
    fila = tabla_recorrido.find_element(By.TAG_NAME, 'tr')
    celdas = fila.find_elements(By.TAG_NAME, 'td')

    #Se crea un indice para recorrer las celdas de la paginación del sitio
    i=-1
    #se crea una lista para almacenar las futuras concesiones
    data = []
    #ciclo genérico de las celdas y almacenamiento de datos
    for celda in celdas:
        i +=1 #incremento del índice
        #Al avanzar en la paginación, es necesario recargar los elementos del DOM. Esto sin embargo, puede hacerse con una función aparte
        tabla_recorrido = driver.find_element(By.XPATH, '/html/body/font/form/p[4]/font/table')
        fila = tabla_recorrido.find_element(By.TAG_NAME, 'tr')
        celdas = fila.find_elements(By.TAG_NAME, 'td')
        driver.implicitly_wait(10)
        celdas = fila.find_elements(By.TAG_NAME, 'td')

        #se clickea en el siguiente número, para avanzar de pagina
        celdas[i].click()    
        driver.implicitly_wait(10)
        #espera mientras se carga la tabla de datos de las concesiones marítimas
        tabla = driver.find_element(By.XPATH, '/html/body/font/form/div/center/table')
        filas = tabla.find_elements(By.TAG_NAME, 'tr')

        #recorrido por los elementos de la tabla de concesiones
        j = 0 #indice para el recorrido de las filas, inicializa en 0 para saltar los encabezados de la tabla
        for fila in filas:
            j += 1
            if j < len(filas):
                celdas = filas[j].find_elements(By.TAG_NAME, 'td')
                n_concesion = celdas[1].text
                tipo_concesion = celdas[2].text
                comuna = celdas[3].text
                lugar = celdas[4].text
                n_rd = celdas[5].text
                tipo_tramite = celdas[6].text
                concesionario = celdas[7].text
                tipo_vigencia = celdas[8].text
                #se crea diccionario para almacenar los datos en formato JSON
                concesion = {'n_concesion':n_concesion, 'tipo_concesion':tipo_concesion, 
                        'comuna':comuna, 'lugar':lugar, 'n_rd':n_rd, 'tipo_tramite':tipo_tramite,
                        'concesionario':concesionario, 'tipo_vigencia':tipo_vigencia}
                #guardar datos en el modelo de la DB
                modelo_concesion = Concesion.objects.create(nro_concesion = n_concesion,
                                                        tipo_concesion = tipo_concesion,
                                                        comuna = comuna, 
                                                        lugar = lugar,
                                                        n_rd = n_rd,
                                                        tipo_tramite = tipo_tramite,
                                                        concesionario = concesionario,
                                                        tipo_vigencia = tipo_vigencia)
                modelo_concesion.save()
                data.append(concesion)
        # Una espera extra, para evitar que los elementos cambien mucho más rápido de lo que puede cargar la página
        driver.implicitly_wait(10)
    #generación de archivo JSON
    with open('data.json','w') as file:
        json.dump(data, file, indent=4)
    file.close()
    #regresa a la página principal, nota importante, si hace click, nuevamente en el botón, duplicará los datos de la DB
    return redirect('lista')