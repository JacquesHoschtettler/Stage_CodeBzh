from django.urls import path
from . import views

urlpatterns = [
    path('', views.connexion, name="connexion"),
    path('deconnexion/', views.deconnexion, name="deconnexion"),
    path('contact', views.contact, name="contact"),
    path('admin/logout/', views.deconnexion, name="logout_admin"),
    path('contact/return', views.return_from_contact, name="return_from_contact")
]
