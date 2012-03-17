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
                extra_context={'is_search_result':u'搜索结果'},
                )
        else:
            return render_to_response('search/bad_result.html',{'is_non_match':True,'is_search_result':u'搜索结果'})
    else:
        return render_to_response('search/bad_result.html',{'is_search_result':u'搜索结果'})

def posts_by_category(request,category_id):
    category=get_object_or_404(Category,id=category_id)
    queryset=category.post_set.filter(published=True)
    return list_detail.object_list(request,
                                   template_object_name='post',
                                   template_name='blog/post_list.html',
                                   queryset=queryset,
                                   paginate_by=10,
                                   extra_context={'is_category':u'分类 '+category.name},
                                   )

def posts_by_tag(request,tag_id):
    tag=get_object_or_404(Tag,id=tag_id)
    queryset=tag.post_set.filter(published=True)
    return list_detail.object_list(request,
                                   template_object_name='post',
                                   template_name='blog/post_list.html',
                                   queryset=queryset,
                                   paginate_by=10,
                                   extra_context={'is_tag':u'标签 '+tag.name},
                                   )

def posts_by_page(request):
    return list_detail.object_list(
                     request,
                     template_object_name='post',
                     template_name='blog/post_list.html',
                     queryset=Post.objects.filter(published=True),
                     paginate_by=10,
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
                                    extra_context={'is_paginated':False,'is_archive':u'存档 '+year+u'年'+month+u'月'}
                                    )

def post_by_id(request,post_id):
    return list_detail.object_detail(request,
                                     template_object_name='post',
                                     template_name='blog/post_detail.html',
                                     object_id=post_id,
                                     queryset=Post.objects.filter(published=True),
                                     )
