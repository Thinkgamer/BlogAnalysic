from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog_analysic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/$','index.views.index'),
    url(r'^user/(\w+)/$','index.views.user'),
    url(r'^focus/(\w+)/$','index.views.focus'),
    url(r'^fans/(\w+)/$','index.views.fans'),
    url(r'^tuijian/(\w+)/$','index.views.tuijian'),
]
