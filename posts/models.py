from django.db import models

class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.TextField(max_length=30)
    content = models.TextField(max_length=1000)
    post_date = models.DateField('Posting date', auto_now_add=True)
    
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField('Email', unique=True)

    def __str__(self):
        return self.name
