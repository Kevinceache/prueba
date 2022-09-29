from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name_= "inicio"),
    path("salir/", views.salir, name="salir" )
]