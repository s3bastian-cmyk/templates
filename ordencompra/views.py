from django.shortcuts import render
from.models import ordencompra
from.serializers import ordencompraserializer
from  rest_framework import viewsets, generics
class ordencompraleercrear(generics.ListCreateAPIView):
    queryset = ordencompra.objects.all()
    serializer_class = ordencompra.Serializer
class ordencompraeliminarmodificar(generics.destroyretriveupdateAPIView):
    queryset = ordencompra.objects.all()
    serializer_class = ordencompra.Serializer


