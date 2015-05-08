from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from main.views import index, projects
from blog.views import index as blog_index, detail as blog_detail
from about.views import index as about_us, profile, signup

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

    url(r'^profile/edit$', profile, name="profile"),
    url(r'^signup/$', signup, name="signup"),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'main/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),

    url(r'^profile/password$', 'django.contrib.auth.views.password_change', {'post_change_redirect' : '/profile/password/successful', 'template_name': 'about/password_change.html'}),
    url(r'^profile/password/successful$', 'django.contrib.auth.views.password_change_done', {'template_name': 'about/password_change.html'}),

    url(r'^apply/$', RedirectView.as_view(url="http://goo.gl/forms/Qy4AhS9aqp")),
    url(r'^survey/$', RedirectView.as_view(url="http://goo.gl/forms/mesV11nJuQ")),
    url(r'^profile/$', RedirectView.as_view(url="https://goo.gl/YlXAYc")),

    (r'^tinymce/', include('tinymce.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
