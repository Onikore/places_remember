from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class UserPosts(models.Model):
    username = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    title = models.TextField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    pub_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись пользователя'
        verbose_name_plural = 'Записи пользователей'
