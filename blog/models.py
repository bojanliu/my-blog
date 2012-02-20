#-*-coding:utf-8-*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from myblog.tinymce import models as tinymce_models

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
    body=tinymce_models.HTMLField()
    excerpt=tinymce_models.HTMLField()
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
        if self.id >= Post.objects.filter(published=True).order_by('-id')[0].id:
            return True
        
    def is_smallest_id(self):
        if self.id <= Post.objects.filter(published=True).order_by('id')[0].id:
            return True

    def befor_post_title(self):
        return Post.objects.get(id=self.id+1).title

    def after_post_title(self):
        return Post.objects.get(id=self.id-1).title

class Message(models.Model):
    people=models.CharField(max_length=15)
    email=models.EmailField()
    message=models.TextField(max_length=200)
    submit_date=models.DateTimeField(auto_now_add=True)
    ip_address=models.IPAddressField(null=True)
    is_public=models.BooleanField(default=True)
    is_removed=models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s说：%s"%(self.people, self.message[:50])

    class Meta:
        ordering=['-submit_date']

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)








from django.contrib.comments.signals import comment_was_posted
def on_comment_was_posted(sender, comment, request, *args, **kwargs):
    # spam checking can be enabled/disabled per the comment's target Model
    #if comment.content_type.model_class() != Entry:
    #    return

    from django.contrib.sites.models import Site
    from django.conf import settings

    try:
        from akismet import Akismet
    except:
        return

    # use TypePad's AntiSpam if the key is specified in settings.py
    if hasattr(settings, 'TYPEPAD_ANTISPAM_API_KEY'):
        ak = Akismet(
            key=settings.TYPEPAD_ANTISPAM_API_KEY,
            blog_url='http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain
        )
        ak.baseurl = 'api.antispam.typepad.com/1.1/'
    else:
        ak = Akismet(
            key=settings.AKISMET_API_KEY,
            blog_url='http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain
        )

    if ak.verify_key():
        data = {
            'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
            'user_agent': request.META.get('HTTP_USER_AGENT', ''),
            'referrer': request.META.get('HTTP_REFERER', ''),
            'comment_type': 'comment',
            'comment_author': comment.user_name.encode('utf-8'),
        }

        if ak.comment_check(comment.comment.encode('utf-8'), data=data, build_data=True):
            comment.flags.create(
                user=comment.content_object.author,
                flag='spam'
            )
            comment.is_public = False
            comment.save()

comment_was_posted.connect(on_comment_was_posted)
