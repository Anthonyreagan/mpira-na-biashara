# contact/models.py

from django.db import models
from django.utils import timezone  # Import timezone


class ContactMessage(models.Model):
    """
    Represents a message submitted through the website's contact form.
    """
    name = models.CharField(max_length=100, help_text="Name of the sender")
    email = models.EmailField(help_text="Email address of the sender")
    subject = models.CharField(max_length=200, blank=True, help_text="Subject of the message (optional)")
    message = models.TextField(help_text="The content of the message")
    sent_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False, help_text="Indicates if the message has been read by an admin")

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-sent_at']  # Order messages by most recent first

    def __str__(self):
        """
        String representation of the contact message.
        """
        return f"Message from {self.name} ({self.email})"


from django.db import models

# Create your models here.
