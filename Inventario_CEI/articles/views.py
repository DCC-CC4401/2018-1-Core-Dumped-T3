from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Article
from .forms import ArticleForm
from reservations.models import Reservation
from reservations.forms import ReservationForm
from datetime import datetime

# Create your views here.
@login_required(login_url="/users/login/")
def detail(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    if article.is_loaned()

    reservations = Reservation.objects.filter(
        article=article, initial_date__gte=timezone.now(),
        state=1
    ).order_by('initial_date')

    messages={}

    if request.user.registereduser.is_admin:
        form = ArticleForm(instance=article)
    else:
        form = ReservationForm()

    if request.method == 'POST':
        # If the user is an admin we only handle article edit forms.
        if request.user.registereduser.is_admin:
            # Only one form is handled at a time.
            form = ArticleForm(request.POST, request.FILES, instance=article)

            if form.is_valid():
                # Save changes made in the form to the article
                form.save()
        else:
            form = ReservationForm(request.POST)

            start_datetime = datetime.strptime(form.data['day'] + ' ' + form.data['start_time'], "%d/%m/%Y %H:%M")
            end_datetime = datetime.strptime(form.data['day'] + ' ' + form.data['end_time'], "%d/%m/%Y %H:%M")

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
                contained = reservations.filter(
                    state = 1,
                    initial_date__lt=end_datetime,
                    end_date__gt=start_datetime
                )
                if not overlaps_end and not overlaps_start and not contained:
                    reservation.save()
                    messages["Reserva pedida correctamente."] = "success"
                else:
                    messages["La reserva choca con el horario de un préstamo."] = "danger"
                    if overlaps_start:
                        form.add_error('start_time', "Horario dentro de un préstamo. ")
                    if overlaps_end:
                        form.add_error('end_time', "Horario dentro de un préstamo. ")
                    if contained:
                        form.add_error(None, {
                                'start_time': "Horario choca con un préstamo.",
                                'end_time': "Horario choca con un préstamo."
                            }
                        )
            else:
                messages["Ya pediste una reserva en los mismos horarios."] = "danger"
                form.add_error('start_time', "Reserva ya existe en este horario.")
                form.add_error('end_time', "Reserva ya existe en este horario.")

    return render(request, 'articles/detail.html', {'article': article, 'reservations': reservations, 'form': form, 'messages': messages})