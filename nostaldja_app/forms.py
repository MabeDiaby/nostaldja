from django import forms
# from django.forms import fields
from .models import Decades, Fads

class DecadesForm(forms.ModelForm):
    class Meta:
        model = Decades
        fields = (
            'start_year',
        )
class FadsForm(forms.ModelForm):
    class Meta:
        model = Fads
        fields = (
            'name',
            'image_url',
            'description',
            'decade',
        )