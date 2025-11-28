from django.urls import path
from .views import ordencompraleercrear, ordencompraeliminarmodificar
urlpatterns = [
    path('ordencompra/',ordencompraleercrear.as_view(),name = 'ordencompralistcreate'),
    path('ordencompra/<init.pk/', ordencompraeliminarmodificar.as_view(),name = 'ordencompra-defail-update-delete'),
]