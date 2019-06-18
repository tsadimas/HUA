from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Topic


def topics_list(request):
    obj = Topic.objects.all()
    template_name = 'topics/topic_list.html'
    context = {
        'topic': obj
    }
    return render(request, template_name, context)

def select_topic(request):
    #obj = Topic.objects.all().filter(taken=False)
    obj1 = [obj for obj in Topic.objects.all() if not obj.taken]
    print('objects')
    print(obj1)
    template_name = 'topics/topic_assign.html'
    context = {
        'topic': obj1
    }
    return render(request, template_name, context)