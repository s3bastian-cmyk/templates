from django.shortcuts import render
from .models import proveedor
from .serializers import proveedorserializers
from rest_framework import viests, generics
class proveedor(generics.ListcreateAPIView):
    queryset = proveedor.objects.all()
    serializer_class = proveedor.Serializer
class productoeliminarmodificar(generics.destroyretriveupdateAPIView):
    queryset = proveedor.objects.all()
    serializer_class = proveedor.Serializer

