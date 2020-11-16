from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from account.managers import myUserMnager

## class manager mishe haminja ham sakht vali dar ye file managers.py misazim

class User(AbstractBaseUser):
    phone = models.IntegerField(verbose_name=_('Phone Number'), unique=True)
    full_name = models.CharField(max_length=120 , verbose_name=_('full name'))
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = myUserMnager
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin