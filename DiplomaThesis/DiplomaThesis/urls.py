"""DiplomaThesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from userprofiles.models import GAUser
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import logout_then_login


urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='base.html'), name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^accounts/', include('registration.backends.simple.urls')), #to auto activate user after registration
    url(r'^accounts/logout/$', lambda request: logout_then_login(request, "/accounts/login"), name='logout'),
    url(r'^accounts/login/', TemplateView.as_view(template_name='login.html'), name="auth_login"),
    #url(r'^user/', include('userprofiles.urls', namespace='user'), name='user'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)