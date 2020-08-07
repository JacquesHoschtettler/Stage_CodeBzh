from django.shortcuts import render

from .forms import ConnexionForm


def connexion(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
    else:
        form = ConnexionForm()
    return render(request, 'connexion/connexion.html')


