from rest_framework import serializers
from .models import almacen
class almacenserializers(serializers.modelserializer):
    class meta:
     Model = almacen
     fields = [ 'id', 'nombre', 'direccion', 'telefono' 'capacidad_total', ' capacudad_utilizada']