from django import forms
from .models import Topic, TopicInterest
from django.forms.widgets import CheckboxSelectMultiple


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description', 'technologies']


def get_topics():
    return [[x.id, x.title] for x in Topic.objects.all()]


class TopicInterestForm(forms.Form):
    topics = forms.MultipleChoiceField(choices=get_topics, required=True, widget=forms.CheckboxSelectMultiple)

