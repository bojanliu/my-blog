#coding:utf-8
from django.contrib.syndication.feeds import Feed
from myblog.blog.models import Post

class LatestPosts(Feed):
    title=u'NewLiu.com 每一刻的我都是新的！'
    link='http://newliu.com/'
    description=u'来自NewLiu.com的更新'

    def items(self):
        return Post.objects.filter(published=True).order_by('-pub_date')[:5]

    def item_link(self,item):
	return self.link+'post/'+str(item.pk)+'/'
