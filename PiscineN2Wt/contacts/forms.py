from django import forms
from .models import Contact

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=200)
    adresse_email = forms.EmailField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    
    
    class Meta:
        model = Contact
        fields = ['nom', 'message', 'adresse_email']