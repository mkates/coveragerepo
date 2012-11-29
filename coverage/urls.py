from django.conf.urls import patterns, include, url
from owl import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('owl.views',
    # Examples:
    url(r'^$','index'),
    # url(r'^coverage/', include('coverage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings

if settings.DEBUG:
   urlpatterns += staticfiles_urlpatterns() 