from .models import Item, Stat
from django.views.generic import ListView, DetailView

from rest_framework import viewsets
from .serializers import ItemSerializer

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.generics import GenericAPIView

class ItemListView(ListView):
    model = Item
    template_name = "item_list.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "item_detail.html"

class FoodListView(ItemListView):
    def get_queryset(self):
        queryset = super(FoodListView, self).get_queryset()
        return queryset.filter(consumables_type='FOOD')

class UtilityListView(ItemListView):
    def get_queryset(self):
        queryset = super(UtilityListView, self).get_queryset()
        return queryset.filter(consumables_type='UTIL')

class ItemList(ListModelMixin, GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ItemDetail(RetrieveModelMixin, GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
