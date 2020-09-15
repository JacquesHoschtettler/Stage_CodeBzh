from django.shortcuts import render
from django.utils.translation import gettext as _
from django.conf import settings

from .models import LegalNotices
import os

LegalNocticeLabels = {'identification': 'Identification', 'activity': 'Activité',
                      'personnalData': 'Utilisation des données personnelles'}


def legal_notice(request, name):
    notice = LegalNotices.objects.filter(name=name)[0]
    titre = _(LegalNocticeLabels[name])
    NoticeLegale = _("Mentions légales")
    path = os.path.join(settings.TEXT_URL, notice.file.name)
    NoticeFile = open(path, "r")
    NoticeTextRaw = NoticeFile.read().split("\n")
    NoticeText = []
    for notice in NoticeTextRaw:
        if notice != "":
            NoticeText.append(_(notice))
    NoticeFile.close()
    return render(request, 'legal_notice/legal_notice.html', locals())
