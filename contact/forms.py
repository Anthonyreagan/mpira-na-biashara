# contact/forms.py

from django import forms

class ContactForm(forms.Form):
    """
    A simple form for collecting contact messages.
    """
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-input rounded-md shadow-sm block w-full', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input rounded-md shadow-sm block w-full', 'placeholder': 'your@example.com'}))
    subject = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-input rounded-md shadow-sm block w-full', 'placeholder': 'Subject (Optional)'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-textarea rounded-md shadow-sm block w-full', 'rows': 5, 'placeholder': 'Your Message'}))