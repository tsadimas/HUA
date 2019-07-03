from django import template
from topics.models import TopicInterest, Topic

register = template.Library()


@register.simple_tag
def has_interest(user):
    try:
        my_interest = TopicInterest.objects.filter(student=user)
    except TopicInterest.DoesNotExist:
        print('-does not exist-')
        return False
    if my_interest:
        return True
    else:
        return False


@register.simple_tag
def get_interest_id(user):
    try:
        int_id = TopicInterest.objects.get(student=user.id)
    except TopicInterest.DoesNotExist:
        print('-does not exist-')
        return None
    if int_id:
        print('int_id ' + str(int_id.id))
        return int_id.id
    else:
        return None


@register.simple_tag
def has_been_assigned(user):
    try:
        my_assignment = Topic.objects.get(assigned_to=user.id)
    except Topic.DoesNotExist:
        print('-does not exist-')
        return None

    if my_assignment.assigned_to:
        return my_assignment.id
    else:
        return None

