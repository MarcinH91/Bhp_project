from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    price = models.FloatField()

    def __str__(self):
        return f'{self.title} costs {self.price}'


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

