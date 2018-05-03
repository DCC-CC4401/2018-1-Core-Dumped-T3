from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login as login_user

from .forms import LoginForm

# Create your views here.
def login(request):
  next = ""

  if request.GET:
    next = request.GET['next']

  if request.method == 'POST':
    form = LoginForm(request.POST)

    if(form.is_valid()):
      return HttpResponseRedirect(next)
      
  else:
    form = LoginForm()

  return render(request, 'accounts/login.html',{'next': next,})
