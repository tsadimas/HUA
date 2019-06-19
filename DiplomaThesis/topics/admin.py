from django.contrib import admin
from .models import Topic, TopicInterest


# class TopicResource:
#     class Meta:
#         model = Topic
#         default_permissions = ('add', 'change')

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'technologies','supervisor', 'is_taken' )
    exclude = ['supervisor']
    readonly_fields = ['is_taken']

    def is_taken(selfself, obj):
        return obj.taken
    is_taken.boolean = True

    class Meta:
        model = Topic

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.supervisor = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Topic, TopicAdmin)

admin.site.register(TopicInterest)
