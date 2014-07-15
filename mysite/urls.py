from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from mysite.views import hello, current_datetime, display_meta
from django.contrib import admin
#from books import models, views

admin.autodiscover()

from books import views
from books.views import unruly_passengers_csv, hello_pdf, hello_pdf1
from django.contrib.auth.views import login, logout

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
    url(r'^csv/$',unruly_passengers_csv),
    url(r'^pdf/$',hello_pdf),
    url(r'^pdf1/$',hello_pdf1),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout),
)

"""from books.views import ArticleListView

urlpatterns += [
    url(r'^$', ArticleListView.as_view(), name='article-list'),
]"""

"""
from mysite.feeds import LatestEntries, LatestEntriesByCategory

feeds = {
    'latest': LatestEntries,
    'categories': LatestEntriesByCategory,
}

urlpatterns += patterns('',
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}),
)
"""

# The URL /debuginfo/ will only be available if your DEBUG setting is set to True.
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^debuginfo/$', views.debug),
    )
