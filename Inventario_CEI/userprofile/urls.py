from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('test/',views.test, name='test'),
    path('loans/', views.myloans, name='loans'),
    path('home/', views.home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
