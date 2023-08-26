from django.views.generic import ListView

from .models import Property


class HomePageView(ListView):
    model = Property
    template_name = "homeownercz/index.html"
