from django import forms
from .models import Student
from .models import Topic
from .models import ApplicationForDiploma


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'


class ApplicationDiplomaForm(forms.ModelForm):
    class Meta:
        model = ApplicationForDiploma
        fields = '__all__'
