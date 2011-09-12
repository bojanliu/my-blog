from django.conf.urls.defaults import *
from django.views.generic import list_detail,date_based
from myblog.blog.models import *
from myblog.blog.views import *
from django.shortcuts import get_object_or_404
from myblog.blog.feeds import LatestPosts
from django.views.decorators.cache import cache_page

bloghome_info={'queryset':Post.objects.filter(published=True),
               'template_object_name':'post',
                'template_name':'blog/post_list.html',
}

  
archive_info={'month_format':'%m',
              'date_field':'pub_date',
              'template_name':'blog/post_list.html',
              'template_object_name':'post',
              'queryset':Post.objects.filter(published=True),
              
    }

feeds={'latest':LatestPosts,}

urlpatterns = patterns('',
    url(r'^$',cache_page(list_detail.object_list,60*1),bloghome_info),
    url(r'^search/$',search,name='post_search'),
    url(r'^category/(?P<category_id>\d+)/$',cache_page(posts_by_category,60*1),name='posts_by_category'),
    url(r'^tag/(?P<tag_id>\d+)/$',cache_page(posts_by_tag,60*1),name='posts_by_tag'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$',cache_page(date_based.archive_month,60*1),archive_info,name='posts_by_month'),
    url(r'^post/(?P<post_id>\d+)/$',cache_page(post_by_id,60*1),name='post_by_id'),
    url(r'^feeds/(?P<url>.*)/$','django.contrib.syndication.views.feed',{'feed_dict':feeds}),
)
