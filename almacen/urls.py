from django.urls import path
from .views import almacenleercrear, almaceneliminarmodificar
urlpatterns = [
    path('almacen/',almacenleercrear.as_view(),name = 'almacenlistcreate'),
    path('almacen/<init.pk/', almaceneliminarmodificar.as_view(),name = 'almacen-defail-update-delete'),
]