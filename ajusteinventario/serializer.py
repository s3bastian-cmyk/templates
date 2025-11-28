from rest_framework import serializers
from .models import ajusteinventario
class ajusteinventarioserializers(serializers.modelserializer):
    class meta:
     Model = ajusteinventario
     fields = ['id', 'nombre','descripcion', 'codigo', 'categoria',]