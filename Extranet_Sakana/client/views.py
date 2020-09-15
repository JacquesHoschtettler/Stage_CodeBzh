from django.shortcuts import render
from django.utils.translation import ugettext as _


def client(request):
    msg = _("Bienvenue ") + request.user.username + _(" !")
    return render(request, 'client/client.html', locals())
