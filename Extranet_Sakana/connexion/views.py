from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group

from .models import ExtensionUser
from .forms import ConnexionForm


def connexion(request):
    error = False
    try_again = True
    msg = "Bonjour, veuillez saisir vos identifiants, s'il vous plaît."
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                init_again_nb_trials(user)
                return redirect(switch(user))
            else:
                try:
                    user = User.objects.get(username=username)
                    msg, try_again = connexion_error_management(user)
                except User.DoesNotExist :
                    msg = "Votre identifiant n'a pas été reconnu, vous n'êtes pas autorisé à pénétrer"\
                          " dans ce site. <br> Contactez l'administrateur pour vous faire inscrire," \
                          "ou vérifiez l'orthographe de votre identifiant."
                    form = ConnexionForm()
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'connexion/connexion.html', locals())


# ------------------ utilities for the connexion method -------------
def switch(user):
    # switch the user to the view is allowed to.
    if user.is_staff:
        address = "admin/"
    else:
        address = str(*Group.objects.filter(user__username=user.username)) + '/'
    return address


def init_again_nb_trials(user):
    # set the number of trials to the maximum, if it is smaller.
    user_ext = ExtensionUser.objects.filter(user__username=user.username)[0]
    if user_ext.nb_trials < 5:
        user_ext.nb_trials = 5
        user_ext.save()


def connexion_error_management(user):
    try_again = True
    if not user.is_active:
        msg = "Votre compte a été désactivé. \n Veuillez contacter l'administrateur " \
              "du site."
        try_again = False
    else:
        user_ext = ExtensionUser.objects.filter(user__username=user.username)[0]
        user_ext.nb_trials -= 1
        if user_ext.nb_trials <= 0:
            user.is_active = False
            user.save()
            msg = "Votre compte a été désactivé. Veuillez contacter l'administrateur " \
                  "du site."
            try_again = False
            user_ext.nb_trials = 5
        else:
            msg = "Échec de la connexion. Vous avez encore " + str(user_ext.nb_trials) \
                  + " essais pour vous connecter, avant que votre compte soit désactivé"
        user_ext.save()
    return msg, try_again


# ------------------ deconnexion method -------------
def deconnexion(request):
    logout(request)
    form = ConnexionForm()
    return redirect(reverse('connexion'))
