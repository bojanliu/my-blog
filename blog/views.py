# Create your views here.
#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response,get_object_or_404,redirect
from myblog.blog.models import *
from django.views.generic import list_detail
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
                                   )


def posts_by_tag(request,tag_id):
    tag=get_object_or_404(Tag,id=tag_id)
    queryset=tag.post_set.filter(published=True)
    return list_detail.object_list(request,
                                   template_object_name='post',
                                   template_name='blog/post_list.html',
                                   queryset=queryset,
                                   )

def post_by_id(request,post_id):
    return list_detail.object_detail(request,
                                     template_object_name='post',
                                     template_name='blog/post_detail.html',
                                     object_id=post_id,
                                     queryset=Post.objects.filter(published=True),
                                     )    

from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
def post_list(request,page_id='1'):#缺省视图参数
    posts=Post.objects.all()
    after_range_num=5 #当前页前显示5页
    befor_range_num=4 #当前页后显示4页
    try:  #如果请求的页码少于1或者类型错误，则跳转到第1页
        page=int(page_id)
        if page<1:
            page=1
    except ValueError:
        page=1
    paginator=Paginator(posts,2) # 设置post在每页显示的数量，这里为1
    try: #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
        post_list=paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        post_list=paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range=paginator.page_range[page-after_range_num:page+befor_page_num]
    else:
        page_range=paginator.page_range[0:int(page)+befor_range_num]
    return render_to_response('blog/post_list_paginate.html',{'posts':post_list,'page_range':page_range},)
