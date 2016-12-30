from __future__ import unicode_literals

from django.contrib import messages
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView
from sayit.models import Example, Musician
from sayit.forms import OrderForm


class ActionMixin(object):
    # Add message of any level
    def add_message(self, msg, level=messages.INFO):
        messages.add_message(self.request, level, msg)

    # Add success messages for forms evaluated to valid
    def form_valid(self, form):
        if hasattr(self, 'success_msg'):
            self.add_message(self.success_msg, level=messages.SUCCESS)
        return super(ActionMixin, self).form_valid(form)


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


class OrderView(ActionMixin, FormView):
    template_name = 'order.html'
    form_class = OrderForm
    success_url = "/order/"
