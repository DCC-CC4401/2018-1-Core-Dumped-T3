from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.http import HttpResponse

# Create your views here.



def index(request):
    return render(request,'article_search/search.html')