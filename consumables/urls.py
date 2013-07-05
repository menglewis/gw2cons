from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',


    url(r'^food', views.FoodListView.as_view(), name='food_list'),
    url(r'^utility', views.UtilityListView.as_view(), name='utility_list'),
    url(r'^$', views.ItemListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)', views.ItemDetailView.as_view(), name='detail' ),
    url(r'^(?P<slug>[\w-]+)', views.ItemDetailView.as_view(), name='detail' ),

)
