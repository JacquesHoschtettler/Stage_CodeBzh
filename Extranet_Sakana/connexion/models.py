from django.db import models


class Logo(models.Model):
    logo = models.ImageField(upload_to="photos/", default="/photos/logo_Sakana.jpg")
