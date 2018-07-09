from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Article
from .forms import NameEditForm, StatusEditForm, ImageEditForm, DescriptionEditForm
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

    if request.user.registereduser.is_admin:
        forms = {
            'nameEdit': NameEditForm().set_name(article.name),
            'statusEdit': StatusEditForm().set_choice(article.status),
            'imageEdit': ImageEditForm(),
            'descriptionEdit': DescriptionEditForm().set_description(article.description)
        }
    else:
        forms = {'reservation': ReservationForm()}

    if request.method == 'POST':
        # If the user is an admin we only handle article edit forms.
        if request.user.registereduser.is_admin:
            # Only one form is handled at a time.
            if request.POST.get('name'):
                name_form = NameEditForm(request.POST)
                article.name = name_form.data['name']
            elif request.POST.get('status'):
                status_form = StatusEditForm(request.POST)
                article.status = status_form.data['status']
            elif request.POST.get('image'):
                print(request.POST)
                print(request.FILES)
            elif request.POST.get('description'):
                description_form = DescriptionEditForm(request.POST)
                article.description = description_form.data['description']
            # Save even if no changed were made
            article.save()
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

    return render(request, 'articles/detail.html', {'article': article, 'reservations': reservations, 'forms': forms, 'messages': messages})