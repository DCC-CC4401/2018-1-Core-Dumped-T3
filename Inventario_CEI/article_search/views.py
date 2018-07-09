from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from articles.models import Article, Space
from users.models import RegisteredUser
from reservations.models import Reservation
from datetime import datetime
from django.utils.timezone import localtime
import pytz
from django.utils import timezone
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

        if request.GET["item"] == "additems":
            print("hola")
            Article(name="pico", description="asd").save()
            Article(name="gundam", description="asd").save()
            Article(name="doritos", description="asd").save()
            Article(name="pcnuevo", description="asd").save()
        if request.GET["item"] == "addspaces":
            print("hola")
            Space(name="sala 4").save()
            Space(name="sala 5").save()
            Space(name="sala 6").save()
            Space(name="sala 7").save()
        if request.GET["item"] == "addreservations":
            user=RegisteredUser.objects.all()[1]
            place1=Space.objects.all()[0]
            place2=Space.objects.all()[3]
            place3=Space.objects.all()[2]
            print("hola")
            Reservation(space=place1,user=user,initial_date=datetime(2018, 7, 5, 16, 30),end_date=datetime(2018, 7, 5, 18, 0)).save()
            Reservation(space=place2,user=user,initial_date=datetime(2018, 7, 5, 13, 30),end_date=datetime(2018, 7, 5, 14, 30)).save()
            Reservation(space=place3,user=user,initial_date=datetime(2018, 7, 5, 15, 30),end_date=datetime(2018, 7, 5, 17, 0)).save()
            Reservation(space=place3,user=user,initial_date=datetime(2018, 7, 5, 11, 30),end_date=datetime(2018, 7, 5, 15, 30)).save()
    print(request.GET)
    items=resize(items,4,busqueda_avanzada)
    print(items)
    return render(request,'article_search/articles.html',{'items':items[1], 'busqueda_avanzada':busqueda_avanzada,'primeros':items[0]})

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
    timezone.activate('America/Santiago')
    print(timezone.now())
    reservations=[]
    colors=set_colors(locations)
    print(colors)
    locations = resize(locations, 6)[1]
    print(locations)
    for i in res:
        if i.space is not None:
            if i.get_status()!="pendiente":
                reservations.append([str(localtime(i.initial_date)),str(localtime(i.end_date)),i.space.name+"\n"+i.get_status(),i.space.name])
    return render(request, 'article_search/locations.html',{'res':reservations,'colors':colors, "locations":locations})

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
