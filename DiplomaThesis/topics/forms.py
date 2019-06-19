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

    def limit_choices(self):
        value = self.cleaned_data['topics']
        print('value = ')
        print(value)
        if len(value) > 3:
            raise forms.ValidationError("You can't select more than 3 items.")
        return value

