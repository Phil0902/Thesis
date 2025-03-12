from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])

    def __str__(self):
        return f'{self.user.username} Profile'