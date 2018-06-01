from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Article
from reservations.models import Reservation
from reservations.forms import ReservationForm
from datetime import datetime

# Create your views here.
@login_required(login_url="/users/login/")
def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    reservations = Reservation.objects.filter(
        article=article, initial_date__gte=timezone.now(),
        state=1   
    ).order_by('initial_date')
    messages={}

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        start_datetime = datetime.strptime(form.data['day'] + ' ' + form.data['start_time'], "%d/%m/%Y %H:%M")
        end_datetime = datetime.strptime(form.data['day'] + ' ' + form.data['end_time'], "%d/%m/%Y %H:%M")

        for key, value in form.data.items():
            print(key, value)

        reservation = Reservation(
            article=article,
            user=request.user.registereduser,
            is_article=True,
            initial_date=start_datetime,
            end_date=end_datetime,
            state=0
        )

        equivalents = Reservation.objects.filter(
            article=article,
            user=request.user.registereduser, 
            is_article=True,
            initial_date=start_datetime,
            end_date=end_datetime,
            state=0
        )

        if not equivalents:
            overlaps_start = reservations.filter(
                state = 1,
                initial_date__lt=start_datetime,
                end_date__gt=start_datetime
            )
            overlaps_end = reservations.filter(
                state = 1,
                initial_date__lt=end_datetime,
                end_date__gt=end_datetime
            )
            if not overlaps_end and not overlaps_start:
                reservation.save()
                messages["Reserva pedida correctamente."] = "success"
            else:
                messages["La reserva choca con el horario de un préstamo."] = "danger"
                if overlaps_start:
                    form.add_error('start_time', "Horario dentro de un préstamo.")
                if overlaps_end:
                    form.add_error('end_time', "Horario dentro de un préstamo.")
        else:
            messages["Ya pediste una reserva en los mismos horarios."] = "danger"
            form.add_error('start_time', "Reserva ya existe en este horario.")
            form.add_error('end_time', "Reserva ya existe en este horario.")
    else:
        form = ReservationForm()

    return render(request, 'articles/detail.html', {'article': article, 'reservations': reservations, 'form': form, 'messages': messages})