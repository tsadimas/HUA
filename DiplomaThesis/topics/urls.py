from django.urls import path
from .views import TopicView, select_topic, TopicInterestView, TopicDetailView, TopicAssignmentView

app_name = 'topics'

urlpatterns = [
    path('select/<int:pk>/', TopicView.as_view(), name='view'),
    path('select/', select_topic, name='select'),
    path('<int:pk>/', TopicDetailView.as_view(), name='detail'),
    path('select/confirmed/<int:pk>/', TopicInterestView.as_view(), name='confirmed'),
    #path('select/assignment/<int:pk>/', TopicAssignmentView.as_view(), name='assignment')

]
