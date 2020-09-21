from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def consultant(request):
    msg = "Vous êtes bien connecté " + request.user.username + " !"
    return render(request, 'consultant/consultant.html', locals())
