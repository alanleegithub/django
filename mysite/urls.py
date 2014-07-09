from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from mysite.views import hello, current_datetime, display_meta
from django.contrib import admin
admin.autodiscover()

from books import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/$', hello),
    url(r'^meta/$', display_meta),
    url(r'^time/$', current_datetime),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
)
