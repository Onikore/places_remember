import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.urls import reverse


class UserPosts(models.Model):
    username = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    title = models.TextField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    pub_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=128, unique=True, default=uuid.uuid1, verbose_name="URL")

    def __str__(self):
        return f'Запись пользователя: {self.username}'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Запись пользователя'
        verbose_name_plural = 'Записи пользователей'
