from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category, null=True,  max_length=120, on_delete=models.SET_NULL)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.title} from {self.price}'



