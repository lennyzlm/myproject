from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class UserProfiles(models.Model):
    username = models.CharField(max_length=20)
    contents_count = models.IntegerField(default=0)
    follow_count = models.IntegerField(default=0)
    follower_count = models.IntegerField(default=0)
    gender = models.CharField(max_length=2)
    intro = models.CharField(max_length=50)
    birthday = models.DateField()
    icon = models.ImageField(upload_to='icons', blank=True,null=True)

class Contents(models.Model):
    username = models.CharField(max_length=20)
    content = models.TextField(max_length=140)
    comment_count = models.IntegerField(default=0)
    content_time = models.DateTimeField()
    pic = models.ImageField(upload_to='pics', blank=True, null=True)

class Comments(models.Model):
    content_id = models.IntegerField()
    comment_username = models.CharField(max_length=20)
    comment = models.TextField(max_length=100)
    comment_time = models.DateTimeField()

class Follows(models.Model):
    username = models.CharField(max_length=20)
    follow_username = models.CharField(max_length=20)

