# Django
from django.contrib import admin
# Models
from .models import *
# Register your models here.
admin.site.register(Loan)
admin.site.register(Reservation)
