from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class AssignmentApplication(models.Model):
    submitter = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True, verbose_name=_("Φοιτητής")
    )
    topic = models.CharField(verbose_name=_("Τίτλος Πτυχιακής:"), max_length=200)

    class Meta:
        verbose_name = 'Ανάθεση'
        verbose_name_plural = 'Αναθέσεις'

    def save(self, *args, **kwargs):
        u = super(AssignmentApplication, self).save(*args, **kwargs)
        return u

    def get_absolute_url(self):
        return reverse('assignments:view', kwargs={'pk': self.pk})
