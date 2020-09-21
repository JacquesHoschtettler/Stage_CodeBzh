from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required


@login_required
def client(request):
    msg = _("Bienvenue ") + request.user.username + _(" !")
    return render(request, 'client/client.html', locals())
