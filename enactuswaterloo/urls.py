from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from main.views import index, projects, project_details, project_details_old, sponsors, contact
from blog.views import index as blog_index, detail as blog_detail
from about.views import index as our_team, profile, signup

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'enactuswaterloo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name="home"),
    url(r'^team/$', our_team, name="our_team"),

    url(r'^projects/$', projects, name="projects"),
    url(r'^projects/(?P<project_id>[0-9]+)/$', project_details_old, name="project_details_old"),
    url(r'^projects/(?P<project_slug>[\w\-_]+)/$', project_details, name="project_details"),
    url(r'^sponsors/$', sponsors, name="sponsors"),
    url(r'^contact/$', contact, name="contact"),


    # url(r'^blog/$', blog_index, name="blog_index"),
    # url(r'^blog/(?P<title>.+)/$', blog_detail, name="blog_detail"),

    url(r'^profile/edit$', profile, name="profile"),
    url(r'^signup/$', signup, name="signup"),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'main/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),

    url(r'^profile/password$', 'django.contrib.auth.views.password_change', {'post_change_redirect' : '/profile/password/successful', 'template_name': 'about/password_change.html'}),
    url(r'^profile/password/successful$', 'django.contrib.auth.views.password_change_done', {'template_name': 'about/password_change.html'}),

    url(r'^apply/$', RedirectView.as_view(url="https://enactuswaterloo.typeform.com/to/CuA1NV")),
    # url(r'^survey/$', RedirectView.as_view(url="http://goo.gl/forms/mesV11nJuQ")),
    url(r'^profile/$', RedirectView.as_view(url="https://goo.gl/YlXAYc")),
    url(r'^cricketmeeting/$', RedirectView.as_view(url="https://plus.google.com/hangouts/_/gu6xvzw4qzxjtljtmwwl2fgnvia")),
    url(r'^hangout/$', RedirectView.as_view(url="https://plus.google.com/hangouts/_/g6444lvbqoxaizvslva55uzj5ya")),

    url(r'^communicationsmeeting/$', RedirectView.as_view(url="https://plus.google.com/hangouts/_/gzx36h4puv4ibbvihcjo6rq75ya")),
    url(r'^sponsorshipmeeting/$', RedirectView.as_view(url="https://plus.google.com/hangouts/_/g4wqvu2vybndq4dnuqqsedzo6ea")),
    url(r'^financemeeting/$', RedirectView.as_view(url="https://plus.google.com/hangouts/_/gvz5nbllnbdaoq7svcjuuk62d4a")),
    url(r'^ikoecomeeting/$', RedirectView.as_view(url="https://plus.google.com/hangouts/_/g3jeboljhk4ey72b3sbj3heu2ya")),
    url(r'^googledrive/$', RedirectView.as_view(url="https://drive.google.com/folderview?id=0B89FOEzS9BZefndHWXEwcXFzRGdlTjNvUm9rYWwzLUFKMXZEaWp2SGx6cV9nZjkySm9fVk0&usp=sharing")),

    (r'^tinymce/', include('tinymce.urls')),
    (r'^ckeditor/', include('ckeditor.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
