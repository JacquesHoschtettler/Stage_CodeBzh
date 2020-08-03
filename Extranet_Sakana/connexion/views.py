from django.shortcuts import render

from .forms import ConnexionForm
from .models import Logo


def connexion(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
    else:
        form = ConnexionForm()
    logo = Logo.objects.get(pk=1)
    return render(request, 'connexion/connexion.html', {'logo': logo})


