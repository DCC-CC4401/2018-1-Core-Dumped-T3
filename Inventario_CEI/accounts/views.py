from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login as login_user

# Create your views here.
def login(request):
    username=""
    password=""
    next=""

    status=''

    if request.GET:
        next = request.GET['next']

    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            return HttpResponseRedirect(next)
        else:
            status = "Usuario o contraseña equivocados"
                

    return render(request, 'accounts/login.html',{'status': status,'username': username,'next': next,})
