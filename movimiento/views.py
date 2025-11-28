from django.shortcuts import render
from.models import movimiento
from.serializers import movimientoserializer
from rest_framework import viewsts, generics
class movimientoleercrear(generics.ListCreateAPIView):
    queryset = movimiento.objects.all()
    serializer_class = movimiento.Serializer   
class movimientooeliminarmodificar(generics.DestroyRetrieveUpdateAPIView):
    queryset = movimiento.objects.all()
    serializer_class = movimiento.Serializer  

