from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CASCADE, Model, OneToOneField, CharField, ManyToManyField
from django.contrib.auth.models import User
from core.models import Product
from django.db import models
from bootstrap_themes import list_themes
from django.db.models.signals import post_save


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    bought_products = ManyToManyField(Product, blank=True)


class MyModel(models.Model):
    theme = models.CharField(max_length=255, default='default', choices=list_themes())

