from django import forms
from django.utils.translation import gettext as _


class ConnexionForm(forms.Form):
    username = forms.CharField(max_length=30, label=_("Nom d'utilisateur"))
    password = forms.CharField(widget=forms.PasswordInput, label=_("Mot de passe"))


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label=_("Sujet"))
    message = forms.CharField(widget=forms.Textarea, label=_("Message"))
    sender = forms.EmailField(label=_("Votre adresse courriel"))
    backSend = forms.BooleanField(
        help_text=_("Cochez si vous souhaitez obtenir une copie du mail envoyé."), required=False,
        label=_("Copie"))
