# core/views.py

from django.shortcuts import render
from blog.models import BlogPost # Import BlogPost model
from services.models import Service # Import Service model

def home_view(request):
    """
    Renders the homepage, displaying latest blog posts and featured services.
    """
    # Fetch latest 3 published blog posts
    latest_posts = BlogPost.objects.filter(is_published=True).order_by('-published_date')[:3]

    # Fetch latest 3 active services
    featured_services = Service.objects.filter(is_active=True).order_by('name')[:3]

    context = {
        'title': 'Home',
        'latest_posts': latest_posts,
        'featured_services': featured_services,
    }
    return render(request, 'core/home.html', context)

def about_view(request):
    """
    Renders the about us page.
    """
    context = {
        'title': 'About Us'
    }
    return render(request, 'core/about.html', context)