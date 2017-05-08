from __future__ import unicode_literals

import os
from textwrap import dedent

from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.utils.timezone import datetime
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
    success_url = '/order/'

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

            sayit_email = os.environ['EMAIL_HOST_USER']

            # Construct email subject
            today=str(datetime.today())
            today_date=today[2:10].replace('-','')
            today_sec=today[-9:-7]
            invoice_number='{0}-{1}-{2}'.format(today_date,name[:2].upper(),today_sec)
            subject = 'Say It With a Song Order #{0}'.format(invoice_number)

            # Assemble plain text email body
            text_welcome = '''\
                Thanks for contacting Say It With a Song. \
                We're excited to work with you!
                We will be in touch within 48 hours. \
                For your records, please see a copy of your order below.'''
            text_contact = '''\
                Contact Information\n
                Name: {0}
                Email: {1}
                Phone: {2}'''.format(name, email, phone)
            text_product = '''\
                Order Information\n
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
            text_closing = '''\
                Sincerely yours,
                Rachel Sparrow
            '''
            text_content_business = '{0}{1}'.format(
                dedent(text_contact),
                dedent(text_product)
            )
            text_content_customer = '{0}{1}{2}'.format(
                dedent(text_welcome),
                text_content_business,
                dedent(text_closing)
            )

            # Assemble HTML email body
            html_welcome = '''
                <p>Thanks for contacting Say It With a Song.
                We're excited to work with you!
                We will be in touch within 48 hours.<br>
                For your records, please see a copy of your order below.</p>'''
            html_contact = '''
                <p>Contact Information</p>
                <ul>
                    <li>Name: {0}</li>
                    <li>Email: {1}</li>
                    <li>Phone: {2}</li>
                </ul>'''.format(name, email, phone)
            html_product = '''
                <p>Order Information</p>
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
            html_closing = '''
            <p>Sincerely yours,<br>
            Rachel Sparrow</p>
            '''
            html_content_business = '{0}{1}'.format(
                dedent(html_contact),
                dedent(html_product)
            )
            html_content_customer = '{0}{1}{2}'.format(
                dedent(html_welcome),
                html_content_business,
                dedent(html_closing)
            )

            # Create email for business
            msg_business = EmailMultiAlternatives(
                subject=subject,
                body=text_content_business,
                from_email='{0} <{1}>'.format(name, email),
                to=[sayit_email],
                headers={'Reply-To': '{0} <{1}>'.format(
                    name, email)}
            )
            msg_business.attach_alternative(html_content_business, 'text/html')

            # Create messsage for customer
            msg_customer = EmailMultiAlternatives(
                subject=subject,
                body=text_content_customer,
                from_email='Say It With a Song <{0}>'.format(sayit_email),
                to=[email],
                headers={'Reply-To': '{0} <{1}>'.format(
                    'Say It With a Song', sayit_email)}
            )
            msg_customer.attach_alternative(html_content_customer, 'text/html')

            try:
                msg_business.send()
                msg_customer.send()
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
