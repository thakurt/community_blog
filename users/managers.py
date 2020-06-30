# Managers. py  we need to add custom manager by subclassing the BaseUserManager, that uses an email as unique field.

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):

    """
    customuser model manager where email is the unique identifiers for authentications instead of username

    """

    def create_user(self, email, password, **extra_fields):
        """
        create and save the user with given email and password

        """

        if not email:
            raise ValueError(_('The email must be set'))

        email = self.normalize_email(email)
        # Normalize_email is prevent multiple signup using same email.
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        create superuser with given email and password

        """
        extra_fields.setdefault('is_staff', True)
        # is_staff is give full access to use admin pannel
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        return self.create_user(email, password, **extra_fields)
