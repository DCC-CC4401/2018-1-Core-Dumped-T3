# Django
from django.shortcuts import render
from django.views import generic
# Models
from .models import *
# Create your views here.


class ReservationsView(generic.TemplateView):
    template_name = 'reservations/reservations.html'

    def get_context_data(self, **kwargs):
        context = super(ReservationsView, self).get_context_data(
            **kwargs
        )
        context['reservas_pendientes'] = Reservation.objects.filter(
            state=Reservation.PENDIENTE
        )
        context['prestamos'] = Loan.objects.all()
        return context


