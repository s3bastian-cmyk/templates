from django.db import models
class ubicacion (models.Model):
    almacen = models.ForeignKey('almacen.almacen', on_delete=models.CASCADE)
    codigo_ubicacion = models.CharField(max_length=20)
    pasillo = models.CharField(max_length=10)
    estante = models.CharField(max_length=10)
    nivel = models.CharField(max_length=10)
    capacidad = models.DecimalField(max_digits=10, decimal_places=2)