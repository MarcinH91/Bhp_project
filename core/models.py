from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    creation_date = models.DateField()
    price = models.FloatField()
