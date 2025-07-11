# blog/urls.py

from django.urls import path
from . import views

app_name = 'blog' # Namespace for this app's URLs

urlpatterns = [
    path('', views.blog_list_view, name='list'), # URL for listing all blog posts (e.g., /blog/)
    path('<slug:slug>/', views.blog_detail_view, name='detail'), # URL for a single blog post (e.g., /blog/my-first-post/)
]