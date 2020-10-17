from django.contrib.auth.models import User
from django.db import models, transaction
from django_countries.fields import CountryField
from core.models import Product
from accounts.models import Profile


class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    def get_total_item_price(self):
        return self.item.price


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    default = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.default:
            return super(Address, self).save(*args, **kwargs)
        with transaction.atomic():
            user = User.objects.get(username=self.user.username)
            Address.objects.filter(
                default=True,
                user=user
            ).delete()
            return super(Address, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class Order(models.Model):
    ref_code = models.CharField(max_length=150, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField(auto_now=True)
    billing_address = models.ForeignKey(
        Address, related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.ref_code}'

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total
