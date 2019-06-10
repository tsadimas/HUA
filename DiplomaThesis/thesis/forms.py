from django import forms

from .models import ThesisApplication

class ThesisApplicationForm(forms.ModelForm):
    class Meta:
        model = ThesisApplication
        fields = ['semester', 'left_lessons']

