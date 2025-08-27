from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    
    bio = models.TextField(max_length=200, blank=True)
    profile_pic = models.CharField(max_length=2050, blank=True, default='')
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username