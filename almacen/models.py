from django.db import models
class almacen(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=100)
    capacidad_total = models.DecimalField(max_digits=10, decimal_places=2)
    capacudad_utilizada = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
