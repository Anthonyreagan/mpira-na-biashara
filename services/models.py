# services/models.py

from django.db import models

class Service(models.Model):
    """
    Represents a service offered by Mpira na Biashara.
    """
    name = models.CharField(max_length=200, help_text="Name of the service (e.g., 'Football Training', 'Sports Event Management')")
    slug = models.SlugField(unique=True, max_length=200, help_text="A unique slug for the URL (e.g., 'football-training')")
    short_description = models.CharField(max_length=500, help_text="A brief summary of the service")
    long_description = models.TextField(blank=True, null=True, help_text="Detailed description of the service")
    is_active = models.BooleanField(default=True, help_text="Whether the service is currently offered")
    created_at = models.DateTimeField(auto_now_add=True) # Automatically sets on creation
    updated_at = models.DateTimeField(auto_now=True) # Automatically updates on each save

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['name'] # Order services alphabetically by name

    def __str__(self):
        """
        String representation of the service, useful for admin panel.
        """
        return self.name