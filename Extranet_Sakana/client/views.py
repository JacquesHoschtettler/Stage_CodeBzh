from django.shortcuts import render


def client(request):
    msg = "Vous êtes bien connecté " + request.user.username + " !"
    return render(request, 'client/client.html', locals())
