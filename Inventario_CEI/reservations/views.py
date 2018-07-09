# Django
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import localtime
# Models
from .models import Loan
from .models import Reservation
from articles.models import Article
from articles.models import Space
from article_search.views import set_colors, resize
# Create your views here.


class ReservationsView(LoginRequiredMixin, generic.TemplateView):
    login_url = "/users/login/"
    template_name = 'reservations/reservations.html'

    def get_context_data(self, **kwargs):
        context = super(ReservationsView, self).get_context_data(
            **kwargs
        )
        context['reservas_pendientes'] = Reservation.objects.filter(
            state=Reservation.PENDIENTE
        ).order_by('-created_at')
        context['prestamos'] = Loan.objects.all().order_by('-created_at')
        res1 = Reservation.objects.filter(
            is_space=True
        )
        reserva_espacios = []
        for reserva in res1:
            reserva_espacios.append([str(localtime(reserva.initial_date)),
                                      str(localtime(reserva.end_date)),
                                      reserva.space.name+"\n"+reserva.get_status(),
                                      reserva.space.name])
        context['res'] = reserva_espacios
        spaces = Space.objects.all()
        context['colors'] = set_colors(spaces)
        events = []
        context['eventos'] = events
        return context


@login_required(login_url="/users/login/")
def accept_reservation(request):
    if request.method == 'POST':
        reservations = request.POST.getlist('reservations')
        for reservation_id in reservations:
            reservation = Reservation.objects.get(id=reservation_id)
            reservation.state = Reservation.ENTREGADO
            reservation.save()
            if reservation.is_article:
                article = reservation.article
                article.status = Article.PRESTAMO
                article.save()
                loan = Loan.objects.create(
                    article=reservation.article,
                    is_article=True,
                    initial_date=reservation.initial_date,
                    end_date=reservation.end_date,
                    user=reservation.user,
                    created_by=request.user.registereduser
                )
                loan.save()
            if reservation.is_space:
                space = reservation.space
                space.status = Space.PRESTAMO
                space.save()
                loan = Loan.objects.create(
                    space=reservation.space,
                    is_space=True,
                    initial_date=reservation.initial_date,
                    end_date=reservation.end_date,
                    user=reservation.user,
                    created_by=request.user.registereduser
                )
                loan.save()
    return redirect('reservations')


@login_required(login_url="/users/login/")
def reject_reservation(request):
    if request.method == 'POST':
        reservations = request.POST.getlist('reservations')
        for reservation_id in reservations:
            reservation = Reservation.objects.get(id=reservation_id)
            reservation.state = Reservation.RECHAZADO
            reservation.save()
    return redirect('reservations')


@login_required(login_url="/users/login/")
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


@login_required(login_url="/users/login/")
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
