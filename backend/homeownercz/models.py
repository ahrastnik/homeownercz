from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    locality = models.CharField(max_length=128)
    url = models.SlugField(unique=True, max_length=256)
    image_url = models.SlugField(max_length=512)
