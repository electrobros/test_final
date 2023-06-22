from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Jurisprudencia(models.Model):
    #nota, en python se sugiere utilizar el estilo snake_case en vez del CamelCase para nombrar las variables
    #nota importante: se sugiere, usar el atributo unique=True para evitar que hayan datos repetidos de la búsqueda, sin embargo
    #en el raspado, pude percatarme que las jurisprudencias, se repetían en el sitio web, variando solamente las visitas de las 
    #mismas, es por ello que opté por no incluir esa configuración
    id_jurisprudencia = models.IntegerField()
    tipoCausa = models.CharField(max_length=3)
    rol = models.CharField(max_length=255)
    caratula = models.CharField(max_length=255)
    nombreProyecto = models.TextField()
    fechaSentencia = models.CharField(max_length=255)
    descriptores = models.TextField()
    linkSentencia = models.CharField(max_length=255)
    urlSentencia = models.CharField(max_length=255)
    activo = models.BooleanField()
    tribunal = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    relacionada = models.CharField(max_length=255)
    visitas =models.IntegerField()

    #reescritura del método Str, aunque no es necesario, ya que se incluye una nueva vista en el administrador
    def __str__(self):
        return self.caratula
    
    #función que permite manejar la vista de detalle de la jurisprudencia, junto con su Primary Key
    def get_absolute_url(self):
        return reverse("scrapper_detail", kwargs={"pk": self.pk})

class Valores(models.Model):
    #nota, en python se sugiere utilizar el estilo snake_case en vez del CamelCase para nombrar las variables
    id_valor = models.IntegerField(default=None)
    idParametro = models.IntegerField(null=True)
    idItemlista = models.IntegerField(null=True)
    valor = models.TextField(null=True)
    parametro = models.CharField(max_length=255, null=True)
    item = models.CharField(max_length=255, null=True)
    #Esta es una relación many to one, cada jurisprudencia tiene una serie de valores
    idjurisprudencia = models.ForeignKey(Jurisprudencia, on_delete=models.CASCADE, related_name='valores', verbose_name='jurisprudencia')

    #reescritura del método que presenta el identificador del valor, esto para mejorar su lectura
    def __str__(self):
        return self.parametro