from django import forms
from .models import Contacts


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
