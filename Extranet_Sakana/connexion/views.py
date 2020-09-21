from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.utils.translation import ugettext as _

from .models import ExtensionUser
from .forms import ConnexionForm, ContactForm


def connexion(request):
    # Page texts, translated if needed
    browsingTitle = _("Navigation")
    ContactUs = _("Nous contacter")
    globalWarning1 = _("Ce site est privé et protégé.")
    globalWarning2 = _("Toute intrusion non autorisée sera poursuivie selon la loi.")
    connexionTitle = _("Se connecter au site")
    connexionButton = _("Se connecter")

    error = False
    try_again = True
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
                    msg = _("Votre identifiant n'a pas été reconnu, vous n'êtes pas autorisé "
                            "à pénétrer dans ce site. Contactez l'administrateur pour vous "
                            "faire inscrire, ou vérifiez l'orthographe de votre identifiant.")
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
        msg = _("Votre compte a été désactivé. Veuillez contacter l'administrateur "
                "du site.")
        try_again = False
    else:
        user_ext = ExtensionUser.objects.filter(user__username=user.username)[0]
        user_ext.nb_trials -= 1
        if user_ext.nb_trials <= 0:
            user.is_active = False
            user.save()
            msg = _("Votre compte a été désactivé.  Veuillez contacter l'administrateur "
                    "du site.")
            try_again = False
            user_ext.nb_trials = 5
        else:
            msg = _("Échec de la connexion. Vous avez encore ") + str(user_ext.nb_trials) \
                  + _(" essais pour vous connecter, avant que votre compte soit désactivé.")
        user_ext.save()
    return msg, try_again


# ------------------ deconnexion method -------------
def deconnexion(request):
    logout(request)
    form = ConnexionForm()
    return redirect(reverse('connexion'))


# ------------------ contact the team method -------------
def contact(request):
    browsingTitle = _("Navigation")
    Return = _("Retour")
    Sending = _("Envoyer le message")
    Message = _("Nous envoyer un message")
    connected = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if request.user.is_authenticated :
            connected = True
        if form.is_valid:
            subject = form.cleaned_data["subject"]
            sender = form.cleaned_data["sender"]
            message = form.cleaned_data["message"]
            backSend = form.cleaned_data["backSend"]
            send_mail(subject=subject, message=message, from_email=sender, fail_silently=False,
                      recipient_list=["jacques.hoschtettler@gmx.com"])

    form = ContactForm()

    return render(request, 'connexion/contact.html', locals())


def return_from_contact(request):
    user = request.user
    if user.is_active:
        address = str(*Group.objects.filter(user__username=user.username))
        return redirect(reverse(address))
    else:
        return redirect(reverse('connexion'))
