from django.shortcuts import render
from .models import detalleorden
from .serializers import detalleordenSerializer
from rest_framework import viewsets, generics
class   detalleordenLeerCrear(generics.ListCreateAPIView):
    queryset = detalleorden.objects.all()
    serializer_class = detalleordenSerializer   
class   detalleordenEliminarModificar(generics.DestroyRetrieveUpdateAPIView):
    queryset = detalleorden.objects.all()
    serializer_class = detalleordenSerializer
