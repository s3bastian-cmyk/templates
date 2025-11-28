from django.db import models
class ajusteinventario(models.Model):
    tipo_ajuste = [('fisici', 'Inventario', 'Fisico'), ('diferencia', 'Diferencia'), ('caduco', 'Caducado')]
    producto = models.ForeignKey ('producto.', on_delete=models.CASCADE)
    tipo_ajuste = models.CharField(max_length=20, choices=tipo_ajuste)
    cantidad_anterior = models.IntegerField()
    cantidad_nueva = models.IntegerField()
    diferencia = models.IntegerField()
    fecha_ajuste = models.DateTimeField(auto_now_add=True)
    ususario = models.CharField (max_length=100)
    motivo = models.TextField()