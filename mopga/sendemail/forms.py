from django import forms

class ContactForm(forms.Form):
    contact_email = forms.EmailField(required=True)
    sujet = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)