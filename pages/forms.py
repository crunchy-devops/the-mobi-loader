# pages/forms.py
from django import forms
from .models import MobiFile

class MobiFileForm(forms.ModelForm):
    class Meta:
        model = MobiFile
        fields = ['file']

