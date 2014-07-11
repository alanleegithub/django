from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from mysite.views import hello, current_datetime, display_meta
from django.contrib import admin
#from books import models, views

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
    
    url(r'^contact/$', views.contact),
    url(r'^contact/thanks/$', views.contact),

    #url(r'^events/$', views.object_list, {'model': models.Event}),
    #url(r'^blog/entries/$', views.object_list, {'model': models.BlogEntry}),
)

# The URL /debuginfo/ will only be available if your DEBUG setting is set to True.
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^debuginfo/$', views.debug),
    )
