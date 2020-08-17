from django.shortcuts import render


def consultant(request):
    msg = "Vous êtes bien connecté " + request.user.username + " !"
    return render(request, 'consultant/consultant.html', locals())
