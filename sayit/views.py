from __future__ import unicode_literals

from django.views.generic import ListView, TemplateView
from sayit.models import Example, Musician


class HomeView(ListView):
    template_name = 'home.html'
    model = Example
    context_object_name = 'examples'


class HowView(TemplateView):
    template_name = 'how.html'


class MusiciansView(ListView):
    template_name = 'musicians.html'
    model = Musician
    context_object_name = 'musicians'


class OrderView(TemplateView):
    template_name = 'order.html'
