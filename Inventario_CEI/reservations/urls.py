from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.ReservationsView.as_view(), name='reservations'),
]
