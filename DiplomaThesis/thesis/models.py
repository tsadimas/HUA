from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class ThesisApplication(models.Model):
    submitter = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True, verbose_name=_("Φοιτητής")
    )
    semester = models.CharField(verbose_name=_("Τρέχον Εξάμηνο:"), max_length=5)
    left_lessons = models.CharField(verbose_name=_("Υπολοιπόμενα Μαθήματα:"), max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Αίτηση'
        verbose_name_plural = 'Αιτήσεις'

    def save(self, *args, **kwargs):
        u = super(ThesisApplication, self).save(*args, **kwargs)
        return u

    def get_absolute_url(self):
        return reverse('thesis:view', kwargs={'pk': self.pk})
