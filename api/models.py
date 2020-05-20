from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    title       = models.CharField(max_length=200)
    content     = models.TextField()
    claps       = models.IntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    


    def __str__(self):
        return self.title
