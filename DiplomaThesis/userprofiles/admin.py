from django.contrib import admin
from django.contrib.auth import get_user
from django_auth_ldap3_ad.auth import LDAP3ADBackend
from django.conf import settings


# Register your models here.
from .models import GAUser, Student, Topic


class GAUserAdmin(admin.ModelAdmin):
    class Meta:
        model = GAUser


admin.site.register(GAUser, GAUserAdmin)


class TopicResource:
    class Meta:
        model = Topic
        default_permissions = ('add', 'change')


admin.site.register(Student)

admin.site.register(Topic)
