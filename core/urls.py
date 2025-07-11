# core/urls.py

from django.urls import path
from . import views # Import views from the current app

app_name = 'core' # This provides a namespace for your app's URLs

urlpatterns = [
    path('', views.home_view, name='home'), # Maps the root URL of the app (e.g., /) to home_view
    path('about/', views.about_view, name='about'), # Maps /about/ to about_view
]