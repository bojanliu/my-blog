from django.conf.urls.defaults import *
from myblog.blog.models import *
from myblog.blog.views import *
from django.shortcuts import get_object_or_404
from myblog.blog.feeds import LatestPosts
from django.views.decorators.cache import cache_page


feeds={'latest':LatestPosts,}

urlpatterns = patterns('',
    url(r'^$',posts_by_page,name='posts_by_page'),
    url(r'^search/$',search,name='post_search'),
    url(r'^category/(?P<category_id>\d+)/$',posts_by_category,name='posts_by_category'),
    url(r'^tag/(?P<tag_id>\d+)/$',posts_by_tag,name='posts_by_tag'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$',posts_by_month,name='posts_by_month'),
    url(r'^post/(?P<post_id>\d+)/$',post_by_id,name='post_by_id'),
    url(r'^feeds/(?P<url>.*)/$','django.contrib.syndication.views.feed',{'feed_dict':feeds}),
)
