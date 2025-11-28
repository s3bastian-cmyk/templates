from django.db import models
class movimiento(models.Model):
    tipo_movimiento = [('entrada', 'Entrada'), ('salida', 'Salida'), ('ajuste', 'Ajuste'), ('transferencia', 'Transferencia')]
    producto = models.ForeignKey('producto.producto', on_delete=models.CASCADE)
    tipo_movimineto = models.CharFiel(max_length=20, choices=tipo_movimiento)
    cantidad = models.IntegerField()
    ubicacion_origen = models.ForeignKey('ubicacion', on_delete=models.CASCADE, related_name='movimientos_origen', null=True, blank=True)
    ubicacion_destino = models.ForeignKey('ubicacion', on_delete=models.CASCADE, related_name='movimientos_destino', null=True, blank=True)
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
    ususario = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100, null=True, blank=True)
    motivo = models.TextField()

