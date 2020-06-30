from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    # which defines the unique identifier
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# In case for AbstractBaseUser

#from django.contrib.auth.models import PermissionsMixin
#from django.utils import timezone

# class CustomUser(AbstractBaseUser, PermissionsMixin):
    #email = models.EmailField(_('email address'), unique=True)
    #is_staff = models.BooleanField(default=False)
    #is_active = models.BooleanField(default=True)
    #date_joined = models.DateTimeField(default=timezone.now)

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []

    #objects = CustomUserManager()

    # def __str__(self):
        # return self.email

# Added fields for email, is_staff, is_active, and date_joined
