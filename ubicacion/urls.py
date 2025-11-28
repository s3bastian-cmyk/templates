from django.urls import path
from .views import ubicacionleercrear, ubicacioneliminarmodificar
urlpatterns = [
    path('ubicacion/',ubicacionleercrear.as_view(),name = 'ubicacionlistcreate'),
    path('ubicacion/<init.pk/', ubicacioneliminarmodificar.as_view(),name = 'ubicacion-defail-update-delete'),
]