from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog_analysic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^see/$','see.views.see')
]
