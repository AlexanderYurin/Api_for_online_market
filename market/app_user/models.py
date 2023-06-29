from django.contrib.auth.models import  AbstractUser
from django.db import models


class Profile(AbstractUser):
	fullName = models.CharField(blank=True, max_length=256, verbose_name="fullName")
	avatar = models.URLField(blank=True, verbose_name="Avatar")
	phone = models.CharField(blank=True, max_length=11, verbose_name="phone")
