# blog/models.py

from django.db import models
from django.utils import timezone # Import timezone for default creation date

class BlogPost(models.Model):
    """
    Represents a single blog post on the website.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, help_text="A unique slug for the URL (e.g., 'my-awesome-post')")
    content = models.TextField()
    author = models.CharField(max_length=100) # Could be a ForeignKey to a User model later
    published_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True) # Automatically updates on each save
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published_date'] # Order posts by most recent first

    def __str__(self):
        """
        String representation of the blog post, useful for admin panel.
        """
        return self.title