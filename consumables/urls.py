from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = patterns('',
    url(r'^api/(?P<pk>\d+)/$', views.ItemDetail.as_view(), name='api_list'),
    url(r'^api/$', views.ItemList.as_view(), name='api_detail'),

    url(r'^$', views.ItemListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)', views.ItemDetailView.as_view(), name='detail' ),
    url(r'^(?P<slug>[\w-]+)', views.ItemDetailView.as_view(), name='detail' ),
)

urlpatterns = format_suffix_patterns(urlpatterns)
