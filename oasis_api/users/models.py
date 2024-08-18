from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(max_length=30, blank=True)
    region = models.CharField(max_length=100, blank=True)
    interests = models.TextField(blank=True)

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Add custom related name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Add custom related name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

