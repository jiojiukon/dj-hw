from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    price = models.IntegerField(max_length=40)
    image = models.CharField(max_length=800)
    release_date = models.CharField(max_length=40)
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)
        