from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Article
from reservations.models import Loan

# Create your views here.
@login_required(login_url="/users/login/")
def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    loans = Loan.objects.filter(article=article)
    return render(request, 'articles/detail.html', {'article': article, 'loans': loans})