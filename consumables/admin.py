from django.contrib import admin
from .models import Item, Stat, Item_Stat

class ItemStatsInline(admin.TabularInline):
    model = Item_Stat
    extra = 2
    ordering = ['order_number']

class ItemsInline(admin.TabularInline):
    model = Item

class ItemAdmin(admin.ModelAdmin):
    fields = ['name', 'duration', 'buy_cost', 'sell_cost', 'food']
    list_display = ['name', 'duration', 'buy_cost', 'sell_cost', 'food']
    list_display_links = ['name']
    list_editable = ['buy_cost', 'sell_cost']
    #list_filter = ['published', 'updated']
    search_fields = ['name']
    inlines = [ItemStatsInline]


class StatAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
    search_fields = ['name']
    #inlines = [ItemsInline]

class ItemStatAdmin(admin.ModelAdmin):
    fields = ['item', 'stat', 'magnitude', 'order_number']

admin.site.register(Item, ItemAdmin)
admin.site.register(Stat, StatAdmin)
admin.site.register(Item_Stat, ItemStatAdmin)
