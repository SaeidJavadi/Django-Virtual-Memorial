from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class myUserMnager(BaseUserManager):
    def create_user(self, phone, name, password):
        if not phone:
            raise ValueError(_('users must have Phone Number'))
        if not name:
            raise ValueError(_('users must have full name'))

        user = self.model(phone=phone,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, name,password):
        user = self.create_user(phone, name, password)
        user.is_admin =True
        user.save(using=self._db)
        return user