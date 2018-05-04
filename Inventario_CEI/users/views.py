from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login as login_user, logout
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import LoginForm, CreateAccountForm

# Create your views here.
def login(request):

  next = "" # reverse("landing page") # When implemented, redirect by default to the landing page
  status = ""

  if request.GET:
    next = request.GET['next']

  if request.user.is_authenticated:
    return HttpResponseRedirect(next) # Redirect if already logged in.

  if request.method == 'POST':
    if "login" in request.POST:
      form = LoginForm(request.POST)

      if form.is_valid():
        data = form.cleaned_data
        user = authenticate(request, username=data['username'], password=data['password'])
        
        if user is not None:
          login_user(request, user)
          return HttpResponseRedirect(next)
        else:
          status="Rut o contraseña no son correctos."
    elif "register" in request.POST:
      return HttpResponseRedirect(reverse("register") + "?next=" + next)
      
  else:
    form = LoginForm()

  return render(request, 'users/login.html',{'form': form, 'next': next, 'status': status})

def register(request):
  next = ""

  if request.GET:
    next = request.GET["next"]

  if request.user.is_authenticated:
    return HttpResponseRedirect(next) # Redirect if already logged in.

  if request.method == 'POST':
    form = CreateAccountForm(request.POST)

    if "register" in request.POST:
      if form.is_valid():
        data = form.cleaned_data

        valid = True

        # check if username is already registered
        if User.objects.filter(username=data['username']):
          form.add_error("username", "Rut ya se encuentra registrado.")
          valid=False
        
        if data['password'] != data['confirm_password']:
          form.add_error("confirm_password", "Contraseñas son distintas.")
          valid=False

        if valid:
          user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email']
          )
          login_user(request, user)
          return HttpResponseRedirect(next)
    else:
      return HttpResponseRedirect(reverse(login) + "?next=" + next)

  else:
    form = CreateAccountForm()

  return render(request, 'users/register.html', {'form':form, 'next':next})

def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse("login"))