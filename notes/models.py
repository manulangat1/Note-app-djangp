from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class BaseModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)


class Tag(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return self.title
