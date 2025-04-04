from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    tech_stack = models.CharField(max_length=100)
    github_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    likes = models.ManyToManyField(get_user_model(), related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title
