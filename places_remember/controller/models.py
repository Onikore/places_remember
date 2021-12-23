from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    data = models.JSONField(verbose_name='Воспоминания',
                            blank=False,
                            default={})

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
