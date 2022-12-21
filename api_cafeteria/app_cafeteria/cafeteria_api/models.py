from django.db import models


class Cafeteria(models.Model):
    id = models.AutoField(primary_key= True)
    clasificacion = models.CharField(max_length=30, blank= False, null = False)
    nombre_del_producto = models.CharField(max_length=30, blank= False, null = False)
    precio = models.IntegerField()
    image = models.CharField(max_length = 150, blank = False, null = False)
    fecha_de_vencimiento = models.IntegerField()
    fecha_de_expedicion = models.IntegerField()