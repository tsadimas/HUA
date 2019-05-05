
from django.contrib import admin


# Register your models here.
from .models import GAUser, Student


class GAUserAdmin(admin.ModelAdmin):
    class Meta:
        model = GAUser


admin.site.register(GAUser, GAUserAdmin)
