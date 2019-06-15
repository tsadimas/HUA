from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Topic


def topics_list(request):
    obj = Topic.objects.order_by('id')
    template_name = 'topics/topic_list.html'
    context = {
        'topic': obj
    }
    return render(request, template_name, context)
