""" imports from django, models.py and forms.py """
from django.views.generic.edit import CreateView
from .models import ContactUs, Newsletter
from .forms import ContactUsForm, NewsletterForm


# Create your views here.
class ContactUsFormView(CreateView):
    """ view for generating the contact form """
    model = ContactUs
    template_name = "contact/contact.html"
    form_class = ContactUsForm
    success_url = '/'


class NewsletterFormView(CreateView):
    """ view for generating the contact form """
    model = Newsletter
    template_name = "contact/newsletter.html"
    form_class = NewsletterForm
    success_url = '/'
