from rest_framework import serializers
from .models import Cafeteria

class CafateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafeteria
        fields = (
            "id",
            "clasificacion",
            "nombre_del_producto",
            "precio",
            "image",
            "fecha_de_vencimiento",
            "fecha_de_expedicion",
        )
        