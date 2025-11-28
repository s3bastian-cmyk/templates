from django.urls import path
from .views import movimientoleercrear, movimientoliminarmodificar
urlpatterns = [
    path('movimiento/',movimientoleercrear.as_view(),name = 'movimientolistcreate'),
    path('movimiento/<init.pk/', movimientoliminarmodificar.as_view(),name = 'movimiento-defail-update-delete'),
]