from django import template
register=template.Library()
from myblog.blog.models import *
from django.contrib.comments.models import *

@register.inclusion_tag('sidebar/category.html')
def blog_category():
    return {'categories':Category.objects.all(),}

@register.inclusion_tag('sidebar/tag.html')
def blog_tag():
    return {'tags':Tag.objects.all(),}

@register.inclusion_tag('sidebar/archive.html')
def blog_archive():
    return {'archives':Post.objects.filter(published=True).dates('pub_date','month',order='DESC'),}

@register.inclusion_tag('sidebar/link.html')
def links():
    return {'links':Link.objects.all(),}

@register.inclusion_tag('sidebar/recent_comments.html')
def recent_comments():
    return {'recent_comments':Comment.objects.filter(is_public=True).order_by('-submit_date')[:10],}


@register.inclusion_tag('sidebar/recent_posts.html')
def recent_posts():
    return {'recent_posts':Post.objects.filter(published=True).order_by('-pub_date')[:6],}
