from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import ApprovalApplicationCreate, ApprovalApplicationUpdate
from django.views.generic.base import TemplateView

app_name = 'approvals'

urlpatterns = [
    path('<int:pk>/', ApprovalApplicationUpdate.as_view(), name='view'),
    path('create/', ApprovalApplicationCreate.as_view(), name='create'),
    path('status/', TemplateView.as_view(template_name='approvals/approvals_status.html'), name='status'),
]
