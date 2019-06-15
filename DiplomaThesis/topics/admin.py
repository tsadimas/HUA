from django.contrib import admin
from .models import Topic


class TopicResource:
    class Meta:
        model = Topic
        default_permissions = ('add', 'change')


admin.site.register(Topic)
