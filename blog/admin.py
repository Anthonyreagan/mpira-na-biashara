# blog/admin.py

from django.contrib import admin
from .models import BlogPost # Import your BlogPost model

# Register your models here.
admin.site.register(BlogPost)