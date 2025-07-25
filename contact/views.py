# contact/views.py

from django.shortcuts import render, redirect
from django.contrib import messages # For displaying success/error messages
from .forms import ContactForm # Import your ContactForm
from .models import ContactMessage # Import your ContactMessage model

def contact_form_view(request):
    """
    Displays the contact form and handles its submission.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message_content = form.cleaned_data['message']

            # Save to database
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_content
            )

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact:form') # Redirect back to the form or a thank you page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm() # An empty form for GET requests

    context = {
        'form': form,
        'title': 'Contact Us'
    }
    return render(request, 'contact/contact_form.html', context)