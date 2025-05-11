from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.conf import settings

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, user_id, email=None, password=None, **extra_fields):
        if not user_id:
            raise ValueError('The user_id must be set')
        email = self.normalize_email(email)
        user = self.model(user_id=user_id, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(user_id, email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    
    username = None

    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions_set", blank=True)

    user_id = models.CharField(max_length = 30, unique = True)
    nickname = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email'] 

    objects = CustomUserManager() 

    def __str__(self) :
        return self.user_id
    
class Guestbook(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='guestbooks', on_delete=models.CASCADE) 

    writer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='guestbook_written', on_delete=models.CASCADE)
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.writer} → {self.owner}"
