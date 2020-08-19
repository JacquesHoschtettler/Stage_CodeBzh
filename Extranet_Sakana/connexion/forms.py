from django import forms


class ConnexionForm(forms.Form):
    username = forms.CharField(max_length=30, label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")


class ContactForm(forms.Form):
    subjet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(label="Votre adresse e-mail")
    backSend = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir "
                                            "une copie du mail envoyé.", required=False)
