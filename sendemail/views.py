from django.contrib import messages
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from Bhp_project.settings import EMAIL_HOST_USER
from .forms import ContactForm
from .models import Message


class ContactFormView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        subject = form.cleaned_data['subject']
        message = Message(email=email, message=message)
        message.save()


        messages.success(send_mail(subject, message, EMAIL_HOST_USER, recipient_list=email, fail_silently=False), self.request, 'Message received')

        return super().form_valid(form)

class SuccessFormView(FormView):
    template_name = 'success.html'
    form_class = ContactForm
    success_url = '/contact/success'
