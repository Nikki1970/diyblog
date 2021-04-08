from django.db import models

from datetime import date
from django.urls import reverse 
from django.contrib.auth.models import User 

class BlogAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    about_the_author = models.TextField(max_length=400, help_text="Enter your details.")

    def __str__(self):
        return self.about_the_author

class Blog(models.Model):
    title = models.CharField(max_length = 100,help_text="Enter the blog title")
    author = models.ForeignKey(BlogAuthor,on_delete=models.SET_NULL,null=True)
    pub_date = models.DateField(default=date.today)
    detail = models.TextField(max_length = 500,help_text="Describe about the blog")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail',args=[str(self.id)])

class BlogComment(models.Model):
    description = models.TextField(max_length=100,help_text="Comment on it")
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.description


