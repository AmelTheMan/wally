
from django.db import models
from matplotlib import image

class Post(models.Model):
    title = models.CharField(max_length=100)
    video=models.FileField(upload_to="posts",null=True)#stvara folder unutar nekog foldera i sprema sliku tamo
    dowload=models.URLField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True)

    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name=models.CharField(max_length=50)
    text=models.TextField(max_length=300)
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comments")
