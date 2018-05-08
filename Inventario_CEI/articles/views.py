from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Article
from reservations.models import Reservation
from reservations.forms import ReservationForm

# Create your views here.
@login_required(login_url="/users/login/")
def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    reservations = Reservation.objects.filter(article=article, initial_date__gte=timezone.now())

    form = ReservationForm()

    return render(request, 'articles/detail.html', {'article': article, 'reservations': reservations, 'form': form})