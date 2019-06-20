from django.contrib import admin
from django import forms
from .models import Topic, TopicInterest


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'technologies','supervisor', 'is_taken', 'get_students', 'assigned_to')
    exclude = ['supervisor']
    readonly_fields = ['is_taken']

    def get_queryset(self, request):
        qs = super(TopicAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            print('in superuser')
            return qs
        return qs.filter(supervisor=request.user)


    def get_students(self, obj):
        topics =  TopicInterest.objects.filter(topic=obj.id)
        students = [t.student for t in topics]
        print(students)
        return students

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
