from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from main.views import index, about_us, projects
from blog.views import index as blog_index, detail as blog_detail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'enactuswaterloo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name="home"),
    url(r'^about/$', about_us, name="about_us"),
    url(r'^projects/$', projects, name="projects"),

    url(r'^blog/$', blog_index, name="blog_index"),
    url(r'^blog/(?P<id>.+)/$', blog_detail, name="blog_detail"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
