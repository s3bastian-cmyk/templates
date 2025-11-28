from django.db import models
class producto (models.Model):
    estado_producto = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('descontinuado', 'Descontinuado'),
    ]
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ForeignKey('categoria.categoria', on_delete=models.CASCADE)
    proveedor = models.ForeignKey('proveedor.proveedor', on_delete=models.CASCADE)
    sku = models.CharField(max_length=50, unique=True)
    upc = models.CharField(max_length=20, unique=True)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock_minimmo = models.IntegerField()
    stock_maximo = models.IntegerField()
    estado = models.CharField(max_length=20, choices=estado_producto, default='activo')
    unidad_medida = models.CharField(max_length=20)
    peso =  models.DecimalField(max_digits=8, decimal_places=3, null= True, blank=True)
    dimensiones = models.CharField(max_length=50, null= True, blank=True)
