from django.urls import path

from sendemail import views

app_name = 'sendemail'

urlpatterns = [
    path('contact', views.ContactFormView.as_view(), name='contact'),
]