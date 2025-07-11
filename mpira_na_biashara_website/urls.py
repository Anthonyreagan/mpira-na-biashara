# mybusinesswebsite/urls.py

from django.contrib import admin
from django.urls import path, include # Ensure 'include' is imported here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # This line includes all URLs from core/urls.py at the root of your site
]