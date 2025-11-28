from django.urls import path
from .views import detalleordenleercrear, detalleordeneliminarmodificar
urlpatterns = [
    path('almacen/',detalleordenleercrear.as_view(),name = 'detalleordenlistcreate'),
    path('almacen/<init.pk/', detalleordeneliminarmodificar.as_view(),name = 'detalleorden-defail-update-delete'),
]