# Django
from django.contrib import admin
# Models
from .models import *
# Register your models here.
admin.site.register(ArticleLoan)
admin.site.register(ArticleReservation)
admin.site.register(SpaceLoan)
admin.site.register(SpaceReservation)
