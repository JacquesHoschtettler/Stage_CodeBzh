from django.urls import path, include
from . import views

urlpatterns = [
    path('consultant/', views.consultant, name="consultant"),
    path('', include('connexion.urls')),
    ]