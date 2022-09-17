from email.policy import default
from enum import unique
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0, unique=True)
    likes = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.ImageField(default=0, unique=True)

    def __str__(self):
        return self.title