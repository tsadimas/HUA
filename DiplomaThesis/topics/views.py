from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import HttpResponseRedirect
from .models import Topic, TopicInterest
from .forms import TopicInterestForm


class ClassTopicView(UpdateView):
    model = Topic
    fields = {'title', 'supervisor'}
    template_name = 'topics/topic_view.html'


def select_topic(request):
    # obj = Topic.objects.all().filter(taken=False)
    # obj1 = [obj for obj in Topic.objects.all() if not obj.taken]
    # print('objects')
    # print(obj1)
    template_name = 'topics/topic_assign.html'
    # context = {
    #     'topic': obj1
    # }
    if request.method == 'POST':
        form = TopicInterestForm(request.POST)
        if form.is_valid():
            topicinterest_set = TopicInterest (
                student=request.user,
            )
            topicinterest_set.save()

            topics =form.cleaned_data.get('topics')
            topicinterest_set.topic.add(*topics)
            topicinterest_set.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, template_name, {'form': form})

    form = TopicInterestForm()
    return render(request, template_name, {'form': form})

