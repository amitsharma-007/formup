from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField

from users.managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("user email address"), unique=True)
    phone=PhoneField(blank=True, help_text='user phone number')
    firstname=models.CharField(max_length=128, blank=True, null=True)
    lastname=models.CharField(max_length=128, blank=True, null=True)
    gender=models.CharField(max_length=128, blank=True, null=True)
    avatar=models.CharField(max_length=128, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
class Address(models.Model):
    user=models.ForeignKey(to=User, null=True, blank=True , on_delete=models.CASCADE)

class PrimaryAddress(models.Model):
    user=models.ForeignKey(to=User, null=True, blank=True , on_delete=models.CASCADE)
    address=models.OneToOneField(to=Address, null=True, blank=True , on_delete=models.CASCADE)

class Education(models.Model):
    user=models.ForeignKey(to=User, null=True, blank=True, on_delete=models.CASCADE)

class Skill(models.Model):
    user=models.ForeignKey(to=User, null=True, blank=True, on_delete=models.CASCADE)

class Certification(models.Model):
    user=models.ForeignKey(to=User, null=True, blank=True , on_delete=models.CASCADE)

class Experience(models.Model):
    user=models.ForeignKey(to=User, null=True, blank=True, on_delete=models.CASCADE)

class Relative(models.Model):
    user=models.ForeignKey(to=User, null=True, blank=True, on_delete=models.CASCADE)

