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
            permission_student_add = Permission.objects.get(name='Can add Φοιτητής')
            self.user_permissions.add(permission_student_add)
            permission_student_change = Permission.objects.get(name='Can change Φοιτητής')
            self.user_permissions.add(permission_student_change)

        if self.username in settings.PROFESSORS:
            print('is professor')
            self.is_staff = True
            #permission_topic_add = Permission.objects.get(name='Can add Θέμα')
            #self.user_permissions.add(permission_topic_add)

        print(self.first_name)
        print(self.last_name)
        print(u)
        return u  # save needs to return a `User` object, remember!


class Student(models.Model):
    identification_number = models.CharField(verbose_name=_("Όνομα Χρήστη"), max_length=20, unique=True, )
    due_to = models.DateTimeField(default=now, null=True, blank=True)
    secretary = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='secretary')

    def __str__(self):
        return self.identification_number

    class Meta:
        verbose_name = 'Φοιτητής'
        verbose_name_plural = 'Φοιτητές'

    @property
    def get_email(self):
        return self.identification_number + '@hua.gr'

    @property
    def user_name_surname(self):
        user = GAUser.objects.get(username=self)

        "Returns the user's name and surname"
        return user.name_el + ' ' + user.surname_el

    user_name_surname.fget.short_description = "Ονοματεπώνυμο"

    def save(self, *args, **kwargs):
        print('in save')
        for count, thing in enumerate(args):
            print('{0}. {1}'.format(count, thing))

        print('instance_id :' + str(self.identification_number))

        u = super(Student, self).save(*args, **kwargs)
        print('in save student')
        print('student due date')
        print(self.due_to)
        print(now())
        if self.due_to.tzinfo is None or self.due_to.tzinfo.utcoffset(self.due_to) is None:
            self.due_to = pytz.utc.localize(self.due_to)

        if self.due_to < now():
            print('has passed')
            self.due_to = datetime.strptime(settings.NEXT_DUE_DATE, '%Y-%m-%d')
        else:
            print('has not passed')

        print(self.identification_number)


class Topic(models.Model):
    title = models.CharField(verbose_name=_("Τίτλος"), max_length=200, unique=True, )
    description = models.TextField(verbose_name=_("Περιγραφή"), null=False, blank=False)
    technologies = models.CharField(verbose_name=_("Προαπαιτούμενα"), max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Θέμα'
        verbose_name_plural = 'Θέματα'
