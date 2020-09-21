from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib.auth.models import User


class Reports(models.Model):
    file = models.FilePathField(verbose_name=_("Nom du fichier"), path=settings.REPORT_URL,
                                primary_key=True)
    title = models.CharField(verbose_name=_("Titre"), max_length=100)
    author = models.CharField(verbose_name=_("Auteur"), max_length=30)
    date = models.DateField(verbose_name=_("Date"))
    readers = models.ManyToManyField(User, verbose_name=_("lecteurs"))
