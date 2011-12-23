# Create your views here.
#-*-coding:utf-8-*-
from django.shortcuts import render_to_response,get_object_or_404,redirect
from myblog.blog.models import *
from django.views.generic import list_detail,date_based
from django.db.models import Q

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        queryset=Post.objects.filter(Q(title__icontains=q)|Q(body__icontains=q))
        if queryset:
            return list_detail.object_list(
                request,
                template_name='blog/post_list.html',
                template_object_name='post',
                queryset=queryset,
                )
        else:
            return render_to_response('search/non_match.html')
    else:
        return render_to_response('search/invalid_search.html')

def posts_by_category(request,category_id):
    category=get_object_or_404(Category,id=category_id)
    queryset=category.post_set.filter(published=True)
    return list_detail.object_list(request,
                                   template_object_name='post',
                                   template_name='blog/post_list.html',
                                   queryset=queryset,
                                   paginate_by=5,
                                   )

def posts_by_tag(request,tag_id):
    tag=get_object_or_404(Tag,id=tag_id)
    queryset=tag.post_set.filter(published=True)
    return list_detail.object_list(request,
                                   template_object_name='post',
                                   template_name='blog/post_list.html',
                                   queryset=queryset,
                                   paginate_by=5,
                                   )

def posts_by_page(request):
    queryset=Post.objects.all()
    return list_detail.object_list(
                     request,
                     template_object_name='post',
                     template_name='blog/post_list.html',
                     queryset=queryset,
                     paginate_by=5,
                     )

def posts_by_month(request,year,month):
    queryset=Post.objects.filter(published=True)
    return date_based.archive_month(request,
                                    month_format='%m',
                                    date_field='pub_date',
                                    year=year,
                                    month=month,
                                    template_name='blog/post_list.html',
                                    template_object_name='post',
                                    queryset=queryset,
                                    extra_context={'is_paginated':False}
                                    )

def post_by_id(request,post_id):
    return list_detail.object_detail(request,
                                     template_object_name='post',
                                     template_name='blog/post_detail.html',
                                     object_id=post_id,
                                     queryset=Post.objects.filter(published=True),
                                     )
