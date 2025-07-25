# contact/urls.py

from django.urls import path
from . import views

app_name = 'contact' # Namespace for this app's URLs

urlpatterns = [
    path('', views.contact_form_view, name='form'), # URL for the contact form (e.g., /contact/)
]