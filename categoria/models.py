from django.db import models
class categoria(models.Model):
    nombre = models.charfield(max_length=100)
    descripcion = models.textfield()
    codigo = models.charfield(max_length=20, unique=True)
    categoria_padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
