from .models import Item, Stat
from django.views.generic import ListView, DetailView


class ItemListView(ListView):
    model = Item
    template_name = "item_list.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "item_detail.html"

class FoodListView(ItemListView):
    def get_queryset(self):
        queryset = super(FoodListView, self).get_queryset()
        return queryset.filter(food=True)

class UtilityListView(ItemListView):
    def get_queryset(self):
        queryset = super(UtilityListView, self).get_queryset()
        return queryset.exclude(food=True)
