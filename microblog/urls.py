from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# This allows D to introspect your apps,
# find the admin.py file in them,
# and then add it to the existing admin urls.
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
