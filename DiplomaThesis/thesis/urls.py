from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import ThesisApplicationCreate, ThesisApplicationUpdate

app_name='thesis'

urlpatterns = [
    path('<int:pk>/', ThesisApplicationUpdate.as_view(), name='view'),
    path('create/', ThesisApplicationCreate.as_view(), name='create'),
]
