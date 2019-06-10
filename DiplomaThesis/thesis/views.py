from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ThesisApplication
from .forms import ThesisApplicationForm


class ThesisApplicationCreate(CreateView):
    form_class = ThesisApplicationForm
    template_name = 'thesis/thesis_create.html'
    #success_url = ''
    print('--request user --')

    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #
    #     form = ThesisApplicationForm(request.POST)
    #     if form.is_valid():
    #         return self.form_valid(request, form, **kwargs)
    #     else:
    #         return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        print('in invalid')
        return self.render_to_response(
            self.get_context_data(form=form))


class ThesisApplicationUpdate(UpdateView):
    model = ThesisApplication
    fields = '__all__'
    template_name = 'thesis/thesis_create.html'
