from __future__ import unicode_literals

from django.views.generic import ListView, TemplateView
from sayit.models import Example


class HomeView(ListView):
    template_name = 'home.html'
    model = Example
    context_object_name = 'examples'


class HowView(TemplateView):
    template_name = 'how.html'


class MusiciansView(TemplateView):
    template_name = 'musicians.html'


class OrderView(TemplateView):
    template_name = 'order.html'
