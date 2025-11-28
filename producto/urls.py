from django.urls import path
from .views import productoleercrear, productoeliminarmodificar
urlpatterns = [
    path('producto/',productoleercrear.as_view(),name = 'productolistcreate'),
    path('producto/<init.pk/', productoeliminarmodificar.as_view(),name = 'producto-defail-update-delete'),
]