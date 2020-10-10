from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, UserCreationForm
)
from django.db.transaction import atomic
from django.forms import CharField, Form, Textarea, EmailField

from accounts.models import Profile


class SubmittableForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(*self.fields, Submit('submit', 'Submit'))


class SignUpForm(SubmittableForm, UserCreationForm):

    first_name = CharField(max_length=100, help_text='Last Name', required=True)
    last_name = CharField(max_length=100, help_text='Last Name', required=True)
    email = EmailField(max_length=150, help_text='Email', required=True)
    company_name = CharField(max_length=100, required=False,
                             help_text='If you want to receive an invoice, please write your company details')
    company_adress = CharField(max_length=100, required=False)
    nip_number = CharField(max_length=18, required=False)
    regon_number = CharField(max_length=22, required=False)



    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email',
                  'company_name', 'company_adress',
                  'nip_number', 'regon_number']

    def save(self, commit=True, *args, **kwargs):
        user = super().save(commit)
        company_name = self.cleaned_data['company_name']
        company_adress = self.cleaned_data['company_adress']
        nip_number = self.cleaned_data['nip_number']
        regon_number = self.cleaned_data['regon_number']
        profile = Profile(user=user, company_name=company_name, company_adress=company_adress,
                          nip_number=nip_number, regon_number=regon_number)
        profile.save()
        return user

class SubmittableAuthenticationForm(SubmittableForm, AuthenticationForm):
    pass

class SubmittablePasswordChangeForm(SubmittableForm, PasswordChangeForm):
    pass