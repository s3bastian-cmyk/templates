from django.shortcuts import render
from .models import almacen
from .serializers import almacenSerializer
from rest_framework import viewsets, generics
class almacenLeerCrear(generics.ListCreateAPIView):
    queryset = almacen.objects.all()
    serializer_class = almacenSerializer
class almacenEliminarModificar(generics.DestroyRetrieveUpdateAPIView):
    queryset = almacen.objects.all()
    serializer_class = almacenSerializer
