from django.urls import path, include
from . import views

urlpatterns = [
    path('client/', views.client, name="client"),
    path('', include('connexion.urls')),
    ]