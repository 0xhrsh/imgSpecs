from django.db import models


class Upload(models.Model):
    src = models.URLField()
