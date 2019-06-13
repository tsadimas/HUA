from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import ApprovalApplicationCreate, ApprovalApplicationUpdate

app_name = 'approvals'

urlpatterns = [
    path('<int:pk>/', ApprovalApplicationUpdate.as_view(), name='view'),
    path('create/', ApprovalApplicationCreate.as_view(), name='create'),
]
