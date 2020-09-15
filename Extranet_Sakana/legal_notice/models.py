from django.db import models


class LegalNotices(models.Model):
    name = models.CharField(max_length=30)
    file = models.FileField()
