from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.views.decorators.cache import cache_page

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^captcha/', include('captcha.urls')),
    (r'^grappelli/',include('grappelli.urls')),
    (r'^admin/filebrowser/',include('filebrowser.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH},name='media'),
    (r'^about/$',cache_page(direct_to_template,60*5),{'template':'about.html'}),
    (r'^contact/$','myblog.views.contact'),
    (r'^contact/thanks/$',direct_to_template,{'template':'contact/thanks.html'}),
    (r'^comments/',include('django.contrib.comments.urls')),
    (r'',include('myblog.blog.urls')),
    url(r'^tinymce/',include('tinymce.urls')),
)
