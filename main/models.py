from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom user model for OAuth2 authentication
    Extends Django's AbstractUser to include additional fields if needed
    """
    email = models.EmailField(unique=True)
    profile_picture = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.username
