from django.conf.urls import patterns, url

from curated_resources import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.resource_list),
    url(r'^(?P<resource_slug>[-\w]+)/$', views.detail, name='detail'),
)
