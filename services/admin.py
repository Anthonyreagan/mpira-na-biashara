# services/admin.py

from django.contrib import admin
from .models import Service # Import your Service model

# Register your models here.
admin.site.register(Service)