from django.urls import path
from .views import ajusteinventarioleercrear, ajusteinventarioeliminarmodificar
urlpatterns = [
    path('ajusteinventario/',ajusteinventarioleercrear.as_view(),name = 'ajusteinventariolistcreate'),
    path('ajusteinventario/<init.pk/', ajusteinventarioeliminarmodificar.as_view(),name = 'ajusteinventario-defail-update-delete'),
]