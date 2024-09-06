from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    rh = models.CharField(blank=True , default="Pendiente" , null=True, max_length=50)