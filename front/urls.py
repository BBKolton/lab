from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from front import views

urlpatterns = [
 url(r'^$', views.index),
 url(r'^url/(?P<pk>[0-9]+)/$', views.url),
 url(r'^deleteurl/(?P<pk>[0-9]+)/$', views.deleteurl),
 url(r'^listall/$', views.listall),
 url(r'^login/$', views.login),
 url(r'^logout/$', views.logout),
]

urlpatterns = format_suffix_patterns(urlpatterns)
