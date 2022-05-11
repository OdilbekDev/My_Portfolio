from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    name = models.CharField(max_length=255)
    phone = models.IntegerField(unique=True, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
l
    def __str__(self):
        return self.name

class Home(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class About_Us(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Services(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    icon = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    img = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Blog(models.Model):
    img = models.ImageField(upload_to='Blog/')
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)


class Team_Member(models.Model):
    avatar = models.ImageField(upload_to='Team/Member/')
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    email = models.URLField()
    insta = models.URLField()
    tg = models.URLField()
    github = models.URLField()

class Contact_Us(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

