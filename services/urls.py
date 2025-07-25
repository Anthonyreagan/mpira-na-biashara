# services/urls.py

from django.urls import path
from . import views

app_name = 'services' # Namespace for this app's URLs

urlpatterns = [
    path('', views.service_list_view, name='list'), # URL for listing all services (e.g., /services/)
    path('<slug:slug>/', views.service_detail_view, name='detail'), # URL for a single service (e.g., /services/football-training/)
]