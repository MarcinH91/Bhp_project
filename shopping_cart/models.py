from django.contrib.auth.models import User
from django.db import models

from core.models import Product
from accounts.models import Profile


# class OrderItem(models.Model):
#     product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
#     is_ordered = models.BooleanField(default=False)
#     date_added = models.DateTimeField(auto_now=True)
#     date_ordered = models.DateTimeField(null=True)
#
#     def __str__(self):
#         return self.product.name


class OrderProduct(models.Model):
    pass


class Order(models.Model):
    ref_code = models.CharField(max_length=150, null=True)
    # owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ref_code}'
