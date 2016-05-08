from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog_analysic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/(\w+)/$','blog.views.blog'),
    url(r'^btuijian/(\w+)/$','blog.views.btuijian'),
    url(r'^paiming/(\w+)/$','blog.views.paiming'),
    url(r'^guidang/(\w+)/$','blog.views.guidang'),
    url(r'^content/(\w+)/(\w+)/(\w+)/$','blog.views.content'),
]
