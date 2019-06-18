from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


SEMESTER_CHOICES = (
    ('06', '06'),
    ('07', '07'),
    ('08', '08'),
    ('09', '09'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
)


class ApprovalApplication(models.Model):
    submitter = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True, verbose_name=_("Φοιτητής")
    )
    semester = models.CharField(verbose_name=_("Τρέχον Εξάμηνο:"), max_length=5, choices=SEMESTER_CHOICES)
    left_lessons = models.CharField(verbose_name=_("Υπολοιπόμενα Μαθήματα:"), max_length=200, null=True, blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Έγκριση'
        verbose_name_plural = 'Εγκρίσεις'

    def __str__(self):
        return self.submitter.username

    def save(self, *args, **kwargs):
        u = super(ApprovalApplication, self).save(*args, **kwargs)
        return u

    def get_absolute_url(self):
        return reverse('approvals:view', kwargs={'pk': self.pk})


