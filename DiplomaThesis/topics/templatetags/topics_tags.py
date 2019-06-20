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

@register.simple_tag
def get_interest_id(user):
    int_id = TopicInterest.objects.get(student=user.id)
    print('int_id ' + str(int_id.id))
    return int_id.id
