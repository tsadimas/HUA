from django import forms
from .models import Student
from .models import Topic


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('__all__')


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('__all__')


class UpdateView(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('__all__')


