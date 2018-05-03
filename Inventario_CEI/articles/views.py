from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Article

# Create your views here.
@login_required
def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {'article': article})