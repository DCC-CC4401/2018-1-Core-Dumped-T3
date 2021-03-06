from django.contrib.auth.decorators import login_required
from reservations.models import Loan, Reservation
from users.models import RegisteredUser
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import FormChangePassword



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


@login_required(login_url="/users/login/")
def delete(request, id=None):
    if request.method == 'POST':
        pklist = request.POST.getlist('custcheck')
        for who in pklist:
            Reservation.objects.get(pk=who).delete()
    return redirect(home)

@login_required(login_url="/users/login/")
def changepass(request):
    if request.method == 'POST':
        form = FormChangePassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña cambiada')
            return redirect(home)
        else:
            messages.error(request, 'Corrija este error porfavor')
    else:
        form = FormChangePassword(request.user)
    return render(request, 'userprofile/changepass.html', {'form': form})