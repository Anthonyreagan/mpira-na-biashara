# team/urls.py
from django.urls import path
from . import views

app_name = 'team' # Define the app namespace

urlpatterns = [
    path('', views.team_list, name='list'),
    path('<slug:slug>/', views.team_detail, name='detail'), # NEW: Detail view path
]