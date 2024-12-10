from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['libro', 'contenido']
        widgets = {'fecha': forms.DateInput(attrs=  {'type':'date'})}