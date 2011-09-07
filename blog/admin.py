from django.contrib import admin
from myblog.blog.models import *
class Postadmin(admin.ModelAdmin):
    filter_horizontal=('categories','tags',)
    list_display=('title','published','pub_date','id')
    date_hierarchy='pub_date'

    def save_model(self,request,obj,form,change):
        if not change:
            obj.author=request.user
        obj.save()

class Linkadmin(admin.ModelAdmin):
    list_display=('name','url','id')

admin.site.register(Link,Linkadmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,Postadmin)
