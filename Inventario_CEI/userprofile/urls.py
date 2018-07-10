from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('changepassword/', views.changepass, name='changepass'),
    path('delete/', views.delete, name='delete'),
    path('loans/', views.myloans, name='loans'),
    path('reservations/', views.home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
