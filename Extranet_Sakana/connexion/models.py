from django.db import models
from django.contrib.auth.models import User


class ExtensionUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nb_trials = models.IntegerField(default=5)

    class Meta:
        verbose_name = "Nombre d'essais"

    def __str__(self):
        return "L'utilisateur \"{0}\" a {1} essai(s) de connexion possible(s) " \
               "avant d'être désactivé".format(self.user.username, self.nb_trials)
