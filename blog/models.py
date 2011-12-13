#-*-coding:utf-8-*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Link(models.Model):
    name=models.CharField(max_length=50)
    url=models.URLField(max_length=150)
    def __unicode__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Post(models.Model):
    author=models.ForeignKey(User,related_name='posts')
    title=models.CharField(max_length=100)
    body=models.TextField()
    excerpt=models.TextField()
    published=models.BooleanField(default=False)
    pub_date=models.DateTimeField('Date Published',auto_now_add=True)
    up_date=models.DateTimeField('Date Updated',auto_now=True)
    categories=models.ManyToManyField(Category,blank=True,null=True)
    tags=models.ManyToManyField(Tag,blank=True,null=True)

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering=['-pub_date']

    def is_bigest_id(self):
        if self.id >= Post.objects.order_by('-id')[0].id:
            return True

    def befor_post_title(self):
        return Post.objects.get(id=self.id+1).title

    def after_post_title(self):
        return Post.objects.get(id=self.id-1).title
