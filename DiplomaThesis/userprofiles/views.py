from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, UpdateView, ListView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from datetime import datetime

from .models import GAUser, TITLE_CHOICES
# Create your views here.


class GAUserDetailView(DetailView):
    model = GAUser


class ApplicantDetailView(DetailView):
    model = GAUser


class GAUserUpdateView(UpdateView):
    model = GAUser
    fields = ['name_el', 'name_en', 'surname_el', 'surname_en', 'title']

    def get_success_url(self):
        return reverse('user:profile', kwargs={"pk": self.object.id})

    def get_form(self, form_class=None):
        form = super(GAUserUpdateView, self).get_form(form_class)
        form.fields['name_el'].required = True
        form.fields['name_en'].required = True
        form.fields['surname_el'].required = True
        form.fields['surname_en'].required = True
        form.fields['title'].required = True
        return form


def check(request):

    print(request.user)
    print(datetime.now())
    result = Student.objects.filter(identification_number=request.user, due_to__gte=datetime.now())
    print(result)
    if result:
        return HttpResponseRedirect(reverse('user:profile', kwargs={'pk': request.user.id}))
    else:
        return HttpResponseRedirect(reverse('user:forbidden'))


def has_complete_profile(user):
    gauser = GAUser.objects.get(id=user.id)
    if gauser.name_el and gauser.name_en and gauser.surname_el and gauser.surname_en and gauser.department and gauser.title and gauser.father_name_el and gauser.father_name_en:
        print('complete profile')
        if gauser.title in [item[0] for item in TITLE_CHOICES]:
            return True
        else:
            return False
    else:
        print('not complete profile')
        return False


