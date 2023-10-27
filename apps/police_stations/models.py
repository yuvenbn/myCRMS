from django.db import models
from django.conf import settings

# Create your models here.

class PoliceStation(models.Model):
    admin = models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
