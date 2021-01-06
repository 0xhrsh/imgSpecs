from django.db import models


class Upload(models.Model):
    src = models.URLField()


class Ans(models.Model):
    logo_border = models.CharField(max_length=500)
    dominant_color = models.CharField(max_length=50)
