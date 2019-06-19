from django.urls import path
from .views import TopicView, select_topic, TopicInterestView

app_name = 'topics'

urlpatterns = [
    path('select/<int:pk>/', TopicView.as_view(), name='view'),
    path('select/', select_topic, name='select'),
    path('select/confirmed/<int:pk>/', TopicInterestView.as_view(), name='confirmed')

]
