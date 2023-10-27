

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from apps.police_stations.models import PoliceStation

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name,phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.CharField(max_length=50, null=False, unique=True)   
    user_level = models.CharField(max_length=20, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.email

class Administrator(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Police(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='admin')
    policeID = models.CharField(max_length=10, null=True, unique=True)
    police_station = models.ForeignKey(PoliceStation, on_delete=models.CASCADE, null=True) 

class RegularUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)



# user levels
#     - admin
#     - police
#     - user