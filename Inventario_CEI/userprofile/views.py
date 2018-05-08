from django.contrib.auth.decorators import login_required
from reservations.models import Loan, Reservation
from users.models import RegisteredUser
from django.shortcuts import render, get_object_or_404


# Create your views here.
@login_required(login_url="/users/login/")
def home(request):
    thisuser = get_object_or_404(RegisteredUser, user_id=request.user.id)
    fullreservations = (Reservation.objects.filter(user=thisuser)).order_by('-initial_date')
    reservations = fullreservations[:10]
    return render(request, 'userprofile/reservations.html', {'reservations': reservations})


@login_required(login_url="/users/login/")
def myloans(request):
    thisuser = get_object_or_404(RegisteredUser, user_id=request.user.id)
    fullloans = (Loan.objects.filter(user=thisuser)).order_by('-initial_date')
    loans = fullloans[:10]
    return render(request, 'userprofile/loans.html', {'loans': loans})


def test(request):
    return render(request, 'userprofile/test.html', {})
