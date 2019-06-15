from django.urls import path
from .views import topics_list

app_name = 'topics'

urlpatterns = [
    #path('/<int:pk>/', topics_list, name='view'),
    path('', topics_list, name='list'),
]