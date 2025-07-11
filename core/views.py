# core/views.py

from django.shortcuts import render

def home_view(request):
    """
    Renders the homepage of the website for Mpira na Biashara.
    """
    return render(request, 'core/home.html', {'title': 'Home'})

def about_view(request):
    """
    Renders the About Us page for Mpira na Biashara.
    """
    return render(request, 'core/about.html', {'title': 'About Us'})