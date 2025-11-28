from django.urls import path
from .views import categorialeercrear, categorialiminarmodificar
urlpatterns = [
    path('categoria/',categorialeercrear.as_view(),name = 'categorialistcreate'),
    path('categoria/<init.pk/', categorialiminarmodificar.as_view(),name = 'categoria-defail-update-delete'),
]