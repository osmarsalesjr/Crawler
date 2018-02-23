from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    usuario = models.ForeignKey(User, related_name='Post', on_delete= models.CASCADE)
    text = models.CharField(max_length=255)
    date_post = models.DateField()

class Timeline(models.Model):
    posts = models.ForeignKey("Post", related_name='post_da_timeline', on_delete=models.CASCADE)