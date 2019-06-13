from django import forms
from .models import ApprovalApplication


class ApprovalApplicationForm(forms.ModelForm):
    class Meta:
        model = ApprovalApplication
        fields = ['semester', 'left_lessons']
