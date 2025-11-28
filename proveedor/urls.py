from django.urls import path
from .views import proveedorleercrear, proveedoreliminarmodificar
urlpatterns = [
    path('proveedor/',proveedorleercrear.as_view(),name = 'proveedorlistcreate'),
    path('proveedor/<init.pk/', proveedoreliminarmodificar.as_view(),name = 'proveedor-defail-update-delete'),
]