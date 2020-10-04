from django.views.generic import ListView

class IndexView(ListView):
    title = 'Welcome to Django Movies!'
    template_name = 'index.html'