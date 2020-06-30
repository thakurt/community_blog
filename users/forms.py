from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):

        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:

        model = CustomUser
        fields = ('email',)


# 1. AbstractUser is like working with the exsisting fields in django and also you can add new fields like email, first_name, Last_name and many more But, The thing is username will be the unique field.

# 2. AbstractBaseUser will help you to get rid of username and make email as unique filed.

# Username field is none for AbstarctUser
# Username field does not exits for AbstractBaseUser
