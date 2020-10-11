from django.db import models


class Message(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=300)