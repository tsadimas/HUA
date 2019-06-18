from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

import datetime

now = datetime.datetime.now()


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

    def _is_taken(self):
        taken = len(TopicAssignment.objects.all().filter(topic=self.id))
        if taken > 0:
            return True
        else:
            return False
    taken=property(_is_taken)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Θέμα'
        verbose_name_plural = 'Θέματα'


class TopicInterest(models.Model):
    student = models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name=_("Φοιτητής"), related_name='student',
                                on_delete=models.CASCADE)
    topic = models.ForeignKey(to=Topic, verbose_name=_("Θέμα"), related_name='topic', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)


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
