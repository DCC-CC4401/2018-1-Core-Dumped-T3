from django.urls import path

from . import views

urlpatterns = [
    path('articles/', views.index,name='LP_articles'),
    path('locations/',views.locations,name='LP_locations'),
    #path('upd/',views.update),
]