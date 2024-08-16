from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.text import slugify
from custom.managers import MyUserManager
from django.contrib.auth.models import PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='online_shop/user/images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def get_name(self):
        if self.username:
            return self.username
        return self.email.split('@')[0] # ['john','gmail.com']

    def __str__(self):
        return self.email