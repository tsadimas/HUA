from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from romanize import romanize
from django.conf import settings
import pytz

try:
    from django.utils import timezone
    now = timezone.now
except ImportError:
    from datetime import datetime
    now = datetime.now


TITLE_CHOICES = (
    ('Προπτυχιακός Φοιτητής', 'Προπτυχιακός Φοιτητής'),
    ('Μεταπτυχιακός Φοιτητής', 'Μεταπτυχιακός Φοιτητής'),
    ('Υποψήφιος Διδάκτωρ', 'Υποψήφιος Διδάκτωρ'),
)


class GAUser(AbstractUser):
    department = models.CharField(verbose_name=_("Τμήμα"), blank=True, null=True,
                                  max_length=100, )
    title = models.CharField(verbose_name=_("Τίτλος"), blank=True, null=True, max_length=100, choices=TITLE_CHOICES)
    title_ldap = models.CharField(verbose_name=_("Τίτλος"), blank=True, null=True, max_length=100, )
    name_el = models.CharField(verbose_name=_("Όνομα στα Ελληνικά"), blank=True, null=True, max_length=100, )
    name_en = models.CharField(verbose_name=_("Όνομα στα Αγγλικά"), blank=True, null=True, max_length=100, )
    surname_el = models.CharField(verbose_name=_("Επώνυμο στα Ελληνικά"), blank=True, null=True, max_length=100, )
    surname_en = models.CharField(verbose_name=_("Επώνυμο στα Αγγλικά"), blank=True, null=True, max_length=100, )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Χρήστης'
        verbose_name_plural = 'Χρήστες'

    def save(self, *args, **kwargs):
        print('instance_id :' + str(self.pk))

        if not self.name_el:
            self.name_el = self.first_name.capitalize()
            self.name_en = romanize(self.name_el)
        if not self.surname_el:
            self.surname_el = self.last_name.capitalize()
            self.surname_en = romanize(self.surname_el)
        if not self.title:
            self.title = self.title_ldap
        u = super(GAUser, self).save(*args, **kwargs)

        if self.username in settings.SECRETARIES:
            print('is secretary')
            self.is_staff = True
            permission_topic_view = Permission.objects.get(name='Can view Θέμα')
            self.user_permissions.add(permission_topic_view)
            permission_approvals_view = Permission.objects.get(name='Can view Έγκριση')
            self.user_permissions.add(permission_approvals_view)
            permission_approvals_change = Permission.objects.get(name='Can change Έγκριση')
            self.user_permissions.add(permission_approvals_change)

        if self.username in settings.PROFESSORS:
            print('is professor')
            self.is_staff = True
            permission_topic_add = Permission.objects.get(name='Can add Θέμα')
            self.user_permissions.add(permission_topic_add)
            permission_topic_change = Permission.objects.get(name='Can change Θέμα')
            self.user_permissions.add(permission_topic_change)
            permission_topic_view = Permission.objects.get(name='Can view Θέμα')
            self.user_permissions.add(permission_topic_view)
            permission_topic_delete = Permission.objects.get(name='Can delete Θέμα')
            self.user_permissions.add(permission_topic_delete)

        print(self.first_name)
        print(self.last_name)
        #print(u)
        return u  # save needs to return a `User` object, remember!


