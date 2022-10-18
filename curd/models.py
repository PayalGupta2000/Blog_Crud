from telnetlib import AUTHENTICATION
from django.db import models
from django.contrib.auth.models import User




# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Product(models.Model):
    Title=models.CharField(max_length=20)
    Image=models.URLField()
    Description=models.TextField()
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Title

    
class Blog(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    Title=models.CharField(max_length=40)
    Image=models.ImageField(upload_to="media/Blog")
    Description=models.TextField()
    

    def __str__(self):
        return self.Title
    
