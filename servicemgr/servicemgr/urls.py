from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'servicemgr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    #(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
