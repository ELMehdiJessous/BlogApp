from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE, null=False,blank=False)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blogpost_likes")
    
    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()