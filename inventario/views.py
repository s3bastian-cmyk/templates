from django.shortcuts import render
from .models import inventario
from.serializers import inventarioserializers
from rest_framework import viewsts, generics 
class inventarioleercrear(generics.ListCreateAPIView):
    queryset = inventario.objects.all()
    serializer_class = inventario.Serializer
class categoriaEliminarModificar(generics.DestroyRetrieveUpdateAPIView):
    queryset = inventario.objects.all()
    serializer_class = inventario.Serializer
