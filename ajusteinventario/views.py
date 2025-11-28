from django.shortcuts import render
from.models import ajusteinventario
from.serializers import ajusteinventarioSerializer
from rest_framework import viewsets, generics 
class ajusteinventarioleercrear(ListcreateAPIView):
    quelyset = ajusteinventario.objects.all()
    serializer_class = ajusteinventarioSerializer
class ajusteinventarioeliminarmodificar(generics.destroyretriveupdateAPIView):
    quelyset = ajusteinventario.objects.all()
    serializer_class = ajusteinventarioSerializer
