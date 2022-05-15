from django.contrib import admin
from .models import ContactUs


admin.site.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """ contact forms sorted by date in admin panel """
    list_display = ("date")