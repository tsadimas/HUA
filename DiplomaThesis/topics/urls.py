from django.urls import path
from .views import topics_list, select_topic

app_name = 'topics'

urlpatterns = [
    #path('/<int:pk>/', topics_list, name='view'),
    path('', topics_list, name='list'),
    path('select/', select_topic, name='select'),

]