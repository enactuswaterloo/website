from django.conf.urls import patterns, include, url
from django.contrib import admin

from main.views import index, about_us

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'enactuswaterloo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index, name="home"),

    url(r'^$', about_us, name="about_us"),
)
