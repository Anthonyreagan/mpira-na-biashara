# contact/admin.py

from django.contrib import admin
from .models import ContactMessage # Import your ContactMessage model

# Register your models here.
admin.site.register(ContactMessage)