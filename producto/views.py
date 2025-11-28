from django.shortcuts import render
from.models import producto 
from.serializers import productoserializer
from rest_framework import viewsts, generics
class producto(generics.ListcreateAPIView):
    queryset = producto.objects.all()
    serializer_class = producto.Serializer
class productoeliminarmodificar(generics.destroyretriveupdateAPIView):
    queryset = producto.objects.all()
    serializer_class = producto.Serializer