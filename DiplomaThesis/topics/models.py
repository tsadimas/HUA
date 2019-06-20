from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed
from threadlocals.threadlocals import get_current_request
from django.db.models import Q
from userprofiles.models import GAUser
import re
import datetime


def filter_students():
    request = get_current_request()
    print(request.META['PATH_INFO'])
    topics = TopicInterest.objects.all()
    students = [t.student for t in topics]

    from urllib.parse import urlparse
    parsed = urlparse(request.META['PATH_INFO'])
    print('scheme  :', parsed.scheme)
    print('netloc  :', parsed.netloc)
    print('path    :', parsed.path)
    print('params  :', parsed.params)
    print('query   :', parsed.query)
    print('fragment:', parsed.fragment)
    print('username:', parsed.username)
    print('password:', parsed.password)
    print('hostname:', parsed.hostname)
    print('port    :', parsed.port)
    numbers = re.findall('\d+', parsed.path)
    print('NUMBER ' + str(numbers))
    print('request')
    print(request)
    a= Topic.objects.filter(Q(supervisor=request.user))
    print(a)
    topic = Topic.objects.get(pk=numbers[0])
    ti = TopicInterest.objects.filter(topic=topic)
    print('ti')
    print(ti)
    print('pk')
    return {'topicinterest__in': ti}
#
class Topic(models.Model):


    supervisor = models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name=_("Καθηγητής"), related_name='supervisor'
                                   , on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_("Τίτλος"), max_length=200, unique=True, )
    description = models.TextField(verbose_name=_("Περιγραφή"), null=False, blank=False)
    technologies = models.CharField(verbose_name=_("Προαπαιτούμενα"), max_length=200)
    supervisor_member_1 = models.CharField(verbose_name=_("Δεύτερο Μέλος Τριμελούς Επιτροπής"), blank=True, null=True
                                           , max_length=100, )
    supervisor_member_2 = models.CharField(verbose_name=_("Τρίτο Μέλος Τριμελούς Επιτροπής"), blank=True, null=True
                                           , max_length=100, )
    assigned_to = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("Φοιτητής"), null=True, blank=True,
        limit_choices_to=filter_students
    )

    def _is_taken(self):
        if self.assigned_to:
            return True
        else:
            return False
    taken = property(_is_taken)

    def __str__(self):
        return self.title

    @property
    def students(self, obj):
        topics =  TopicInterest.objects.filter(topic=obj.id)
        students = [t.student for t in topics]
        print(students)
        return students

    class Meta:
        verbose_name = 'Θέμα'
        verbose_name_plural = 'Θέματα'


class TopicInterest(models.Model):
    student = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("Φοιτητής")
    )
    topic = models.ManyToManyField(Topic)
    timestamp = models.DateTimeField(default=now)

    class Meta:
        verbose_name = 'Ενδιφέρεται'
        verbose_name_plural = 'Ενδιαφέρονται'

    def __str__(self):
        return self.student.username

def regions_changed(sender, **kwargs):
    if kwargs['instance'].topic.count() > 1:
        raise ValidationError("You can't assign more than three topics")


m2m_changed.connect(regions_changed, sender=TopicInterest.topic.through)


class TopicAssignment(models.Model):
    student = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("Φοιτητής")
    )
    topic = models.OneToOneField(
        Topic,
        on_delete=models.CASCADE,
        verbose_name=_("Θέμα")
    )
