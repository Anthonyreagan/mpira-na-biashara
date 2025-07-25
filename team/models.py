# team/models.py
from django.db import models
from django.utils.text import slugify

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100, blank=True) # NEW: Slug field
    title = models.CharField(max_length=100) # e.g., "CEO", "Head of Marketing"
    bio = models.TextField()
    image = models.ImageField(upload_to='team_members/', blank=True, null=True) # Images will go into media/team_members/
    # Optional: Social media links
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    # Add more social links as needed (e.g., facebook_url, instagram_url)

    class Meta:
        ordering = ['name'] # Order team members alphabetically by name
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug: # Auto-generate slug if not provided
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)