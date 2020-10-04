from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CASCADE, Model, OneToOneField, CharField
from django.contrib.auth.models import User

# Create your models here.
class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    shoes = CharField(max_length=2)