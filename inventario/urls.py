from django.urls import path
from .views import inventarioleercrear, inventarioeliminarmodificar
urlpatterns = [
    path('inventario/',inventarioleercrear.as_view(),name = 'inventariolistcreate'),
    path('inventraio/<init.pk/', inventarioeliminarmodificar.as_view(),name = 'inventario-defail-update-delete'),
]