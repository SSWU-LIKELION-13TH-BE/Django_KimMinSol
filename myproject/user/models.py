from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

class CustomUser(AbstractUser):
    
    username = None

    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions_set", blank=True)

    user_id = models.CharField(max_length = 30, unique = True)
    nickname = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = 'user_id'

    def __str__(self) :
        return self.user_id
    
class Guestbook(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='guestbooks', on_delete=models.CASCADE) 

    writer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='guestbook_written', on_delete=models.CASCADE)
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.writer} → {self.owner}"
