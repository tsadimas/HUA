from django import template
from topics.models import TopicInterest

register = template.Library()


@register.simple_tag
def has_interest(user):
    my_interest = TopicInterest.objects.filter(student=user)
    if my_interest:
        return True
    else:
        return False
