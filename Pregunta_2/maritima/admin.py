from django.contrib import admin
from .models import Concesion

#vista basada en clases para mostrar la información obtenida en el administrador de Django
# Register your models here.
class ConcesionAdmin(admin.ModelAdmin):
    #Campos que se desplegaran en la vista del administrador
    list_display = ('nro_concesion', 'tipo_concesion', 'lugar', 'tipo_vigencia')
    #filtro de la concesión por número y lugar
    list_filter = ('nro_concesion', 'lugar')
    #campos aceptados para buscar la concesion
    search_fields = ('nro_concesion', 'n_rd')

#registro de vista en el administrador
admin.site.register(Concesion, ConcesionAdmin)
