
from django.db import models


class Register(models.Model):
    username = models.CharField(max_length=200)
    email= models.EmailField(max_length=254,default=False)
    password= models.CharField(max_length=100)
    re_password = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    intro=models.TextField(null=True)
    description=models.TextField()
    created_on=models.DateTimeField(auto_now=True)
    image=models.FileField(max_length=200)
    author=models.CharField(max_length=200)





    class Meta:
        ordering=['-created_on']

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=200)
    created_on=models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200)





    class Meta:
        ordering=['-created_on']







