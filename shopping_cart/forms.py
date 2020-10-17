from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('B', 'Blik'),
    ('P', 'PayPal'),
    ('O', 'Przelew'),
    ('K', 'Karta')
)


class CheckoutForm(forms.Form):
    billing_address = forms.CharField(required=False, initial='ul. Krakowska 5')
    billing_country = CountryField(default='PL' ,blank_label='(wybierz kraj').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False, initial='00-000')
    billing_city = forms.CharField(required=False, initial='Warszawa')

    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)