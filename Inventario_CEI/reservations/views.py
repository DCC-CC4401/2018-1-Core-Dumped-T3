# Django
from django.shortcuts import render, redirect
from django.views import generic
# Models
from .models import Loan
from .models import Reservation
from articles.models import Article
from articles.models import Space
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
    if request.method == 'POST':
        loans = request.POST.getlist('loans')
        for loan_id in loans:
            loan = Loan.objects.get(id=loan_id)
            loan.state = Loan.PERDIDO
            loan.save()
            if loan.is_article:
                article = loan.article
                article.status = Article.PERDIDO
                article.save()
    return redirect('reservations')


def change_loan_to_received(request):
    if request.method == 'POST':
        loans = request.POST.getlist('loans')
        for loan_id in loans:
            loan = Loan.objects.get(id=loan_id)
            loan.state = Loan.RECIBIDO
            loan.save()
            if loan.is_article:
                article = loan.article
                article.status = Article.DISPONIBLE
                article.save()
            if loan.is_space:
                space = loan.space
                space.status = Space.DISPONIBLE
                space.save()
    return redirect('reservations')

