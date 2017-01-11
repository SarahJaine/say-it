from __future__ import unicode_literals

from textwrap import dedent

from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
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

    def post(self, request, *args, **kwargs):
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            name = order_form.cleaned_data['name']
            email = order_form.cleaned_data['email']
            phone = order_form.cleaned_data['phone_hidden']

            product = order_form.cleaned_data['product']
            product_language = order_form.cleaned_data['language']
            product_occasion = order_form.cleaned_data['occasion']
            product_date = order_form.cleaned_data['date']
            product_recipient = order_form.cleaned_data['recipient']
            product_relationship = order_form.cleaned_data['relationship']
            product_style = order_form.cleaned_data['style']
            message = order_form.cleaned_data['message']
            message = message.replace('\r\n', '\n                ')

            recipient_list = ['orders@sayitwithasong.co']

            # Assemble body of message
            text_contact = '''\
                Contact Information\n
                Name: {0}
                Email: {1}
                Phone: {2}'''.format(name, email, phone)
            text_order = '''\
                Product Order Information\n
                Product: {0}
                Language: {1}
                Occasion: {2}
                Date: {3}
                Recipient: {4}
                Relationship to Recipient: {5}
                Style: {6}
                Message:
                {7}'''.format(product, product_language,
                              product_occasion, product_date,
                              product_recipient, product_relationship,
                              product_style, message)
            text_content = '{0}\n\n{1}'.format(dedent(text_contact),
                                               dedent(text_order))

            # Assemble alternative HTML version of message
            html_contact = '''\
                <h1>Order from {0}</h1>
                <h2>Contact Information</h2>
                <ul>
                    <li>Name: {0}</li>
                    <li>Email: {1}</li>
                    <li>Phone: {2}</li>
                </ul>'''.format(name, email, phone)
            html_order = '''\
                <h2>Product Order Information</h2>
                <ul>
                    <li>Product: {0}</li>
                    <li>Language: {1}</li>
                    <li>Occasion: {2}</li>
                    <li>Date: {3}</li>
                    <li>Recipient: {4}</li>
                    <li>Relationship to Recipient: {5}</li>
                    <li>Style: {6}</li>
                    <li>Message: {7}</li>
                </ul>'''.format(product, product_language,
                                product_occasion, product_date,
                                product_recipient, product_relationship,
                                product_style, message)
            html_content = '{0}\n\n{1}'.format(dedent(html_contact),
                                               dedent(html_order))

            # Create message
            msg = EmailMultiAlternatives(
                subject='Order from {0}'.format(
                    name),
                body='{0}\n\n{1}'.format(dedent(text_contact),
                                         dedent(text_order)),
                from_email=email,
                to=recipient_list,
                headers={'Reply-To': '{0} <{1}>'.format(
                    name, email)}
            )
            msg.attach_alternative(html_content, "text/html")

            try:
                msg.send()
                self.add_message(
                    'Your order was sent!',
                    level=messages.SUCCESS)
                return self.form_valid(order_form)

            except:
                self.add_message(
                    'Something went wrong. Please try again.',
                    level=messages.ERROR)
                return self.form_invalid(order_form)

        else:
            self.add_message(
                'Error found. Please try again.',
                level=messages.ERROR)
            return self.form_invalid(order_form)
