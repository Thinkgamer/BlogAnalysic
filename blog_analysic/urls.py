from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog_analysic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('login.urls')),
    url(r'^index/', include('index.urls')),
    url(r'^see/', include('see.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^', "blog_analysic.views.change")
]
