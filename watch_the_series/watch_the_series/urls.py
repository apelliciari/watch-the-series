from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('series.views',
    # Examples:
     url(r'^$', 'home', name='home'),
     url(r'^login/$', 'login_view', name='login_view'),
     url(r'^search/$', 'search', name='search'),
     url(r'^create/(?P<thetvdb_id>\d+)/$', 'create', name='create'),
     url(r'^serial/(?P<slug>[^/]+)/$', 'serial', name='serial'),
     url(r'^watch/(?P<serial_id>\d+)/(?P<episode>\d+)/(?P<season_number>\d+)/$', 'watch', name='watch'),
    # url(r'^watch_the_series/', include('watch_the_series.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
