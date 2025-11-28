from django.db import models
class inventario (models.Model):
    producto = models.ForeignKey('producto.producto', on_delete=models.CASCADE)
    ubicacion = models.ForeignKey('ubicacion.ubicacion', on_delete=models.CASCADE)
    cantidad_disponible = models.IntegerField()
    cantidad_reservada = models.IntegerField(default=0)
    cantidad_ordenada = models.IntegerField(default=0)
    fecha_actualizacion = models.DateTimeField(max_lenght=50,auto_now=True)
    
