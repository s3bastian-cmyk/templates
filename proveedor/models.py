from django.db import models
class proveedor(models):
    nombre_empresa = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    direccion = models.TextField()
    nuc = models.CharField(max_length=20, unique=True)
    tipo_proveedor = models.CharField(max_length=50, choices=[('nacional', 'nacional'), ('internacional', 'Internacional'),])
    clasificaccion =  models.DecimalField(max_digits=3, decimal_places=2, default=0)
