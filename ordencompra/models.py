from django.db import models
class ordencompra (models.Model):
    estado_orden  = [ ('borrador', 'Borrador'), ('enviada', 'Enviada'), ('parcial', 'Recibida', 'Parcialmente'), ('completada', 'Completada'), ('cancelada', 'Cancelada')]
    numero  = models.CharField(max_length=20, unique=True)
    proveedor = models.ForeignKey('proveedor.proveedor', on_delete=models.CASCADE)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    fecha_esperada = models.DateField()
    estado = models.CharField(max_length=20, choices=estado_orden, default='borrador')
    subtiotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    notas = models.TextField(null=True, blank=True)
