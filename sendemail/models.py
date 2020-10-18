from django.core.mail import EmailMessage
from django.db import models

from Bhp_project import settings


class Message(models.Model):

    email = EmailMessage(models.EmailField(max_length=254),settings.EMAIL_HOST_USER,
        ["marcin.sopot@gmail.com"],
    )

    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=300)