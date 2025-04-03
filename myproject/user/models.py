from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions_set", blank=True)

    user_id = models.CharField(max_length = 30, unique = True)
    nickname = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = 'user_id'

    def __str__(self) :
        return self.user_id
