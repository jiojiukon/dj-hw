from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=800)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.CharField(max_length=40)
    lte_exists = models.BooleanField()
    slug = models.SlugField(default="", null=False)
