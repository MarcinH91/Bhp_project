from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CASCADE, Model, OneToOneField, CharField, EmailField
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    first_name = CharField(max_length=100, default=None)
    last_name = CharField(max_length=100, default=None)
    email = EmailField(max_length=150, default=None)
    company_name = CharField(max_length=100, null=True)
    company_adress = CharField(max_length=100, null=True)
    nip_number = CharField(max_length=18, null=True)
    regon_number = CharField(max_length=22, null=True)


    def __str__(self):
        return self.user.username






