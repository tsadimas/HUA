from django.urls import path
from .views import ClassTopicView, select_topic

app_name = 'topics'

urlpatterns = [
    path('<int:pk>/', ClassTopicView.as_view(), name='view'),
    path('select/', select_topic, name='select'),

]