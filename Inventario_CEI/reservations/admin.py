from django.contrib import admin
from .models import Reservation, Loan
# Register your models here.
admin.site.register(Loan)
admin.site.register(Reservation)