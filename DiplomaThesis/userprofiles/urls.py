from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from . import views
from . import models

app_name = 'user'

urlpatterns = [
    url(r'^check/$', view=views.check, name='check'),
    url(r'^success/$', TemplateView.as_view(template_name='userprofiles/success.html'), name='success'),
    url(r'^profile/(?P<pk>\w+)/$', view=login_required(views.GAUserDetailView.as_view()), name='profile'),
    url(r'^update/(?P<pk>\w+)/$', view=login_required(views.GAUserUpdateView.as_view()), name='update'),
    url(r'^forbidden/$', TemplateView.as_view(template_name='userprofiles/forbidden.html'), name='forbidden'),
    url(r'^applyfordiploma/(?P<pk>\w+)/$', view=login_required(views.ApplicationUpdate.as_view()),
        name='applyfordiploma'),
    #url(r'^applyfordiploma/$', views.applyfordiploma, name='applyfordiploma'),

]


