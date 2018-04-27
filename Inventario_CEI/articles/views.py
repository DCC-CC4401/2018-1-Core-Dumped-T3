from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Article

# Create your views here.
def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {'article': article})