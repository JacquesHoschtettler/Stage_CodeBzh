from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User

from .forms import ConnexionForm


def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'connexion/connexion.html', locals())


def deconnexion(request):
    logout(request)
    form = ConnexionForm()
    return render(request, 'connexion/connexion.html', locals())
