from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)
from accounts.models.user_manager import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # an admin user; non super-user
    admin = models.BooleanField(default=False)  # an superuser
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.firstname + " " + self.lastname

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        """
        Returns boolean for if a user a staff
        """
        return self.staff

    @property
    def is_admin(self):
        """
        Returns boolean for if a user an admin
        """
        return self.admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
