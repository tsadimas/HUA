from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^', views.home, name='home'),
    #url(r'^accounts/', include('registration.backends.default.urls')), #To send activation code)
    url(r'^account/login/', include('registration.backends.default.urls'), views.login_user, name='login'),
]