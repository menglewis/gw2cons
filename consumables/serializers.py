from django.forms import widgets
from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'duration', 'buy_cost', 'sell_cost', 'consumable_type', 'description')

