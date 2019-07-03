from django import template
from approvals.models import ApprovalApplication

register = template.Library()


@register.simple_tag
def has_approval(user):
    try:
        my_approval = ApprovalApplication.objects.filter(submitter=user)
    except ApprovalApplication.DoesNotExist:
        print('-does not exist-')
        return False
    if my_approval:
        return True
    else:
        return False


@register.simple_tag
def has_been_approved(user):
    try:
        approval = ApprovalApplication.objects.get(submitter=user)
    except ApprovalApplication.DoesNotExist:
        print('-does not exist-')
        return None
    if approval.approved:
        return True
    else:
        return False
