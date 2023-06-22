from django.db import models
from django.urls import reverse

# Create your models here.
class Concesion(models.Model):
    nro_concesion = models.CharField(max_length=145)
    tipo_concesion = models.CharField(max_length=145)
    comuna = models.CharField(max_length=145)
    lugar = models.CharField(max_length=145)
    n_rd = models.CharField(max_length=145)
    tipo_tramite = models.CharField(max_length=145)
    concesionario = models.CharField(max_length=255)
    tipo_vigencia = models.CharField(max_length=145)

    def __str__(self) -> str:
        return self.lugar
    def get_absolute_url(self):
        return reverse("maritima_detail", kwargs={"pk": self.pk})