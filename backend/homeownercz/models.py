from django.db import models


class Property(models.Model):
    url = models.SlugField(
        primary_key=True, max_length=256, help_text='Link to the property listing'
    )
    name = models.CharField(max_length=128, help_text='Name of the property')
    price = models.CharField(max_length=128, help_text='Price of the property')
    locality = models.CharField(max_length=128, help_text='Location of the property')
    image_url = models.SlugField(
        max_length=512, help_text='Link to the image of the property'
    )
