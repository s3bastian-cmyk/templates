from django.shortcuts import render
from .models import ubicacion
from .serializers import ubicacionserializers
from rest_framework import viewsets, generics
class ubicacion(generics.ListcreateAPIView):
    queryset = ubicacion.objects.all()
    serializer_class = ubicacion.Serializer
class productoeliminarmodificar(generics.destroyretriveupdateAPIView):
    queryset = ubicacion.objects.all()
    serializer_class = ubicacion.Serializer
