from __future__ import unicode_literals

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class HowView(TemplateView):
    template_name = 'how.html'


class MusiciansView(TemplateView):
    template_name = 'musicians.html'


class OrderView(TemplateView):
    template_name = 'order.html'
