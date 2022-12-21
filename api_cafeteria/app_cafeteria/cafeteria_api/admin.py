from django.contrib import admin
from .models import Cafeteria
# Register your models here.

class CafeteriaAdmin(admin.ModelAdmin):
    list_display = (
        "clasificacion",
        "nombre_del_producto",
        "precio",
        "image",
        "fecha_de_vencimiento",
        "fecha_de_expedicion",
    )
    
admin.site.register(Cafeteria, CafeteriaAdmin)
