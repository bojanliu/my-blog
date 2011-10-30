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
    url(r'^$',list_detail.object_list,bloghome_info),
    url(r'^search/$',search,name='post_search'),
    url(r'^category/(?P<category_id>\d+)/$',posts_by_category,name='posts_by_category'),
    url(r'^tag/(?P<tag_id>\d+)/$',posts_by_tag,name='posts_by_tag'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$',date_based.archive_month,archive_info,name='posts_by_month'),
    url(r'^post/(?P<post_id>\d+)/$',post_by_id,name='post_by_id'),
    url(r'^feeds/(?P<url>.*)/$','django.contrib.syndication.views.feed',{'feed_dict':feeds}),
)
