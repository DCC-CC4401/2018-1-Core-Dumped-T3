from django.urls import path

from . import views

urlpatterns = [
    path('articulos/', views.index),
    path('espacios/',views.locations),
    #path('upd/',views.update),
]