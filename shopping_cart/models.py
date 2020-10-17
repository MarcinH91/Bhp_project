from django.contrib.auth.models import User
from django.db import models

from core.models import Product
from accounts.models import Profile


class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ordered = models.BooleanField(default=False)

    def get_total_item_price(self):
        return self.item.price



class Order(models.Model):
    ref_code = models.CharField(max_length=150, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ref_code}'

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total
