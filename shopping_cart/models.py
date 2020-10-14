from django.contrib.auth.models import User
from django.db import models

from core.models import Product
from accounts.models import Profile


class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ordered = models.BooleanField(default=False)


class Order(models.Model):
    ref_code = models.CharField(max_length=150, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ref_code}'
