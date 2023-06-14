from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, default='ex@ex.com')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True)
