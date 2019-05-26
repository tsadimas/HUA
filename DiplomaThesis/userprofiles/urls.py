from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from . import views

app_name = 'user'

urlpatterns = [
    url(r'^check/$', view=views.check, name='check'),
    url(r'^profile/(?P<pk>\w+)/$', view=login_required(views.GAUserDetailView.as_view()), name='profile'),
    url(r'^update/(?P<pk>\w+)/$', view=login_required(views.GAUserUpdateView.as_view()), name='update'),
    url(r'^apply_for_diploma/(?P<pk>\w+)/$', TemplateView.as_view(template_name='userprofiles/apply_for_diploma.html'), name='apply_for_diploma'),
    url(r'^forbidden/$', TemplateView.as_view(template_name='userprofiles/forbidden.html'), name='forbidden'),

]
