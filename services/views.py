# services/views.py

from django.shortcuts import render, get_object_or_404
from .models import Service # Import your Service model

def service_list_view(request):
    """
    Displays a list of all active services.
    """
    # Get all services that are marked as active, ordered by name
    services = Service.objects.filter(is_active=True).order_by('name')
    context = {
        'services': services,
        'title': 'Our Services'
    }
    return render(request, 'services/service_list.html', context)

def service_detail_view(request, slug):
    """
    Displays the details of a single service based on its slug.
    Uses get_object_or_404 to return a 404 error if the service is not found.
    """
    # Retrieve the service by its unique slug, and ensure it's active
    service = get_object_or_404(Service, slug=slug, is_active=True)
    context = {
        'service': service,
        'title': service.name
    }
    return render(request, 'services/service_detail.html', context)