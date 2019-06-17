from django import forms
from .models import AssignmentApplication


class AssignmentApplicationForm(forms.ModelForm):
    class Meta:
        model = AssignmentApplication
        fields = ['topic']
