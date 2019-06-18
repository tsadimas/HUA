from django import template
from topics.models import Topic

register = template.Library()


@register.simple_tag
def can_view_topics(user):
    all_topics = Topic.objects.filter(submitter=user)
    if all_topics:
        return True
    else:
        return False

