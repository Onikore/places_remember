from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


def user_directory_path(instance, filename):
    return f'users/user_{instance.user.id}/{instance.user.id}_{filename}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    memories = models.FileField(upload_to=user_directory_path,
                                verbose_name='Воспоминания',
                                auto_created=True)

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
