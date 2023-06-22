from django.contrib import admin
from .models import Jurisprudencia, Valores #importación de modelos al administrador de Django

class ValoresInline(admin.StackedInline):
    model = Valores

#vista del administrador de Django, para observar la jurisprudencia con sus respectivos valores
class JurisprudenciaAdmin(admin.ModelAdmin):
    list_display = ('id_jurisprudencia', 'caratula', 'nombreProyecto', 'urlSentencia')
    #filtro de la jurisprudencia por id y el título de la misma
    list_filter = ('id_jurisprudencia', 'caratula')
    #campos aceptados para buscar la jurisprudencia
    search_fields = ('id_jurisprudencia', 'descriptores')
    inlines = [
       ValoresInline,
    ]

# Register your models here.
admin.site.register(Jurisprudencia, JurisprudenciaAdmin)
admin.site.register(Valores)