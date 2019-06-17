from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import AssignmentApplicationCreate, AssignmentApplicationUpdate

app_name = 'assignments'

urlpatterns = [
    path('<int:pk>/', AssignmentApplicationUpdate.as_view(), name='view'),
    path('create/', AssignmentApplicationCreate.as_view(), name='create'),
]
