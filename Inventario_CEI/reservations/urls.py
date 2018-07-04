from django.urls import path
from django.conf import settings

from .views import ReservationsView
from .views import change_loan_to_received
from .views import change_loan_to_lost
from .views import accept_reservation
from .views import reject_reservation

urlpatterns = [
    path('', ReservationsView.as_view(), name='reservations'),
    path('/loan-received', change_loan_to_received, name='loan-received'),
    path('/loan-lost', change_loan_to_lost, name='loan-lost'),
    path('/reservation-accepted', accept_reservation, name='reservation-accepted'),
    path('/reservation-rejected', reject_reservation, name='reservation-rejected'),
]
