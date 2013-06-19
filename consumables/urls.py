from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',


    url(r'^food', views.FoodListView.as_view(), name='food_list'),
    url(r'^utility', views.UtilityListView.as_view(), name='Utility_list'),
    url(r'^$', views.ItemListView.as_view(), name='list'),
    url(r'^item/(?P<pk>\d+)', views.ItemDetailView.as_view(), name='detail' ),
)
