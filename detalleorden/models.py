from django.db import models
class detalleorden(models.Model):
    orden_compra = models.ForeignKey('ordencompra', on_delete=models.CASCADE)
    producto = models.ForeignKey('producto.', on_delete=models.CASCADE)
    cantidad_ordenada = models.IntegerField()
    cantidad_recibida = models.IntegerField(default=0)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)


