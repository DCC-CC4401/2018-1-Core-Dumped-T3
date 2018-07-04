# Django
from django.shortcuts import render, redirect
from django.views import generic
# Models
from .models import Loan
from .models import Reservation
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


def accept_reservation(request):
    if request.method == 'POST':
        reservations = request.POST.getlist('reservations')
        for reservation_id in reservations:
            reservation = Reservation.objects.get(id=reservation_id)
            reservation.state = Reservation.ENTREGADO
            reservation.save()
    return redirect('reservations')


def reject_reservation(request):
    if request.method == 'POST':
        reservations = request.POST.getlist('reservations')
        for reservation_id in reservations:
            reservation = Reservation.objects.get(id=reservation_id)
            reservation.state = Reservation.RECHAZADO
            reservation.save()
    return redirect('reservations')


def change_loan_to_lost(request):
    pass


def change_loan_to_received(request):
    pass

