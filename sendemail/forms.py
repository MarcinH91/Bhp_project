from django import forms
from django.core.mail import send_mail

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field

# https://data-flair.training/blogs/django-send-email/




class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = 'post'
        self.helper.form_action = '/contact/success'

        self.helper.add_input(Submit('submit', 'Submit'))

    email = forms.EmailField(max_length=254)
    subject = forms.CharField(max_length=100, widget=forms.TextInput)
    message = forms.CharField(max_length=254, widget=forms.Textarea)


