from django.shortcuts import render
from.models import categoria
from.serializers import categoriaSerializer
from rest_framework import viewsets, generics
class categoriaLeerCrear(generics.ListCreateAPIView):
    queryset = categoria.objects.all()
    serializer_class = categoriaSerializer
class categoriaEliminarModificar(generics.DestroyRetrieveUpdateAPIView):
    queryset = categoria.objects.all()
    serializer_class = categoriaSerializer

