from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from heapoverflow import settings


class Tag(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre


class User(AbstractUser):
    user_id = models.CharField(primary_key=True, max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    information = models.CharField(max_length=200)
    familiar_tags = models.ManyToManyField(Tag, related_name='familiar_user')
    studying_tags = models.ManyToManyField(Tag, related_name='studying_user')
    header_image = models.ImageField()
    profile_image = models.ImageField()
    followings = models.ManyToManyField('self', blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.user_id


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='post', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    header = models.CharField(max_length=140)
    body = models.CharField(max_length=10000, blank=True, default='')
    tag = models.ManyToManyField(Tag, 'post')
    posts_to = models.ManyToManyField('self', blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.header


class Image(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
