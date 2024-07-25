# scraper/forms.py
from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label='Website URL', widget=forms.URLInput(attrs={
        'placeholder': 'Enter website URL'
    }))
