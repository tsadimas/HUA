from django import template
from approvals.models import ApprovalApplication

register = template.Library()


@register.simple_tag
def has_approval(user):
    my_approval = ApprovalApplication.objects.filter(submitter=user)
    if my_approval:
        return True
    else:
        return False
