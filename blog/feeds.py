from django.contrib.syndication.feeds import Feed
from myblog.blog.models import Post

class LatestPosts(Feed):
    title='PYnotes.info'
    link='http://www.pynotes.info/'
    description='The updates from PYnotes.info'

    def items(self):
        return Post.objects.filter(published=True).order_by('-pub_date')[:5]

    def item_link(self,item):
	return self.link+'post/'+str(item.pk)+'/'
