""" django and model imports """
from django.contrib import admin
from .models import ContactUs, Newsletter


admin.site.register(ContactUs)
admin.site.register(Newsletter)


class ContactUsAdmin(admin.ModelAdmin):
    """ contact forms sorted by date in admin panel """
    list_display = ("date")
