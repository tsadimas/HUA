from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Topic(models.Model):
    title = models.CharField(verbose_name=_("Τίτλος"), max_length=200, unique=True, )
    description = models.TextField(verbose_name=_("Περιγραφή"), null=False, blank=False)
    technologies = models.CharField(verbose_name=_("Προαπαιτούμενα"), max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Θέμα'
        verbose_name_plural = 'Θέματα'
