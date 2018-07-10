
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from articles.models import Article, Space
from users.models import RegisteredUser
from reservations.models import Reservation
from datetime import datetime
from django.utils.timezone import localtime
import pytz
from django.utils import timezone
from reservations.forms import *
from django.http import HttpResponseRedirect
# Create your views here.
from django.http import HttpResponse

# Create your views here.



@login_required(login_url="/users/login/")
def index(request):
    items=Article.objects.all()
    busqueda_avanzada=False
    if "busqueda_avanzada" in request.GET:
        busqueda_avanzada=True
    if "item" in request.GET:
        items=Article.objects.filter(name__contains=request.GET["item"])

    form=ReservationForm()
    print(request.GET)
    items=resize(items,4,busqueda_avanzada)
    print(items)
    return render(request,'article_search/articles.html',{'items':items[1], 'busqueda_avanzada':busqueda_avanzada,'primeros':items[0],'form':form})


def busqueda(request):
    form = ReservationForm(request.POST)
    search_name=request.POST['search']
    disp=request.POST['disp']
    start_datetime = datetime.strptime(form.data['day'] + ' ' + form.data['start_time'], "%d/%m/%Y %H:%M")
    end_datetime = datetime.strptime(form.data['day'] + ' ' + form.data['end_time'], "%d/%m/%Y %H:%M")
    artic=Article.objects.filter(name__contains =search_name,status=disp)
    articles=[]
    for i in artic:
        overlaps = Reservation.objects.filter(
            state=1,
            article=i,
            initial_date__lt=end_datetime,
            end_date__gt=start_datetime
        )
        if not overlaps:
            articles.append(i)
    items=resize(articles,4,True)
    return render(request,'article_search/articles.html',{'items':items[1], 'busqueda_avanzada':True,'primeros':items[0],'form':form})



@login_required(login_url="/users/login/")
def locations(request):
    res=[]
    locations=Space.objects.all()
    if 'filtrar' in request.GET:
        for r in Reservation.objects.all():
            if r.space is not None:
                if r.space.name in request.GET:
                    print(r.space.name)
                    res.append(r)
    else:
        res=Reservation.objects.all()
    reservations=[]
    colors=set_colors(locations)
    print(colors)
    locations = resize(locations, 6)[1]
    print(locations)
    form=ReservationForm()
    for i in res:
        if i.space is not None:
            if i.get_status()!="pendiente":
                reservations.append([str(localtime(i.initial_date)),str(localtime(i.end_date)),i.space.name+"\n"+i.get_status(),i.space.name])
    return render(request, 'article_search/locations.html',{'res':reservations,'colors':colors, "locations":locations,"form":form})

def make_reservation(request):
    print(request.POST)
    loc = get_object_or_404(Space, id=request.POST["loc"])
    print(loc.name)
    reservations = Reservation.objects.filter(
        space=loc, initial_date__gte=timezone.now(),
        state=1
    ).order_by('initial_date')
    messages = {}
    if request.method == 'POST':
        form = ReservationForm(request.POST)

        start_datetime = datetime.strptime(form.data['day'] + ' ' + form.data['start_time'], "%d/%m/%Y %H:%M")
        end_datetime = datetime.strptime(form.data['day'] + ' ' + form.data['end_time'], "%d/%m/%Y %H:%M")

        for key, value in form.data.items():
            print(key, value)

        reservation = Reservation(
            space=loc,
            user=request.user.registereduser,
            is_space=True,
            initial_date=start_datetime,
            end_date=end_datetime,
            state=0
        )

        equivalents = Reservation.objects.filter(
            space=loc,
            user=request.user.registereduser,
            is_space=True,
            initial_date=start_datetime,
            end_date=end_datetime,
            state=0
        )

        if not equivalents:
            overlaps = reservations.filter(
                state=1,
                initial_date__lt=end_datetime,
                end_date__gt=start_datetime
            )
            if not overlaps:
                reservation.save()
                messages["Reserva pedida correctamente."] = "success"
            else:
                messages["La reserva choca con el horario de un préstamo."] = "danger"
                if overlaps:
                    form.add_error('start_time', "Horario dentro de un préstamo.")
    return redirect('LP_locations')

def set_colors(locations):
    colormap = ["3459F0", "8BA0F4",
                "9708EC", "BA67EB",  # violeta
                "FF5D1C", "FFA682",
                "1AF094", "7DF4C1",
                "F72375", "F7649D",  # rosa
                "FFBB1C", "FFDA82",
                "133DEC", "5D7AF1",
                "FF4900", "FF7F4C",
                "00EC87", "48F2A9",
                "FFB300", "FFCA4C",
                "0729B3", "00B467"]  #muy opacos
    colors={}
    for i in range(len(locations)):
        locations[i].color="#"+colormap[i%len(colormap)]
        colors[locations[i].name]="#"+colormap[i%len(colormap)]
    return colors

def resize(my_array,w, busqueda_avanzada=False):
    new_array=[]
    primeros=[]
    aux=[]
    for i in my_array:
        aux.append(i)
        if (len(aux)==2 and len(primeros)==0 and busqueda_avanzada):
            primeros=aux
            aux=[]
        if len(aux)==w:
            new_array.append(aux)
            aux=[]
    if len(aux)!=0:
        new_array.append(aux)
    return [primeros,new_array]
