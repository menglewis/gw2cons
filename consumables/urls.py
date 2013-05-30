from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',


    url(r'^food', views.FoodListView.as_view(), name='food_list'),
    url(r'^other', views.OtherListView.as_view(), name='other_list'),
    url(r'^$', views.ItemListView.as_view(), name='list'),
    url(r'^item/(?P<pk>\d+)', views.ItemDetailView.as_view(), name='detail' ),
)
