from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, verbose_name=_('Name'))
    last_name = models.CharField(max_length=20, verbose_name=_('Surname'))
    email = models.EmailField(blank=True, verbose_name=_('Email'))
    photo = models.ImageField(upload_to='photos_user/', verbose_name=_('Photo'), blank=True)
    date_registration = models.DateTimeField(auto_now_add=True, verbose_name=_('Date registration'))
    balance = models.IntegerField(default=0, verbose_name=_('Balance'))

    class Meta:
        verbose_name_plural = _('Profiles')
        verbose_name = _('Profile')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



