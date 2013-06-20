import json, urllib2

from django.template.defaultfilters import slugify

from ..models import Item

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gw2cons.settings")

CONSUMABLES_API = "http://www.gw2spidy.com/api/v0.9/json/all-items/3"

ITEM_DETAIL = "https://api.guildwars2.com/v1/item_details.json?item_id="

undead = "http://www.gw2spidy.com/api/v0.9/json/item/8878"

"""
    items = json.loads(urllib2.urlopen(CONSUMABLES_API).read())['results']

    for item in items:
        id = item['data_id']
        official_dump = json.loads(urllib2.urlopen(ITEM_DETAIL + str(id)).read())
        if official_dump['type'] == 'Consumable':
            i = Item(pk=id, name = official_dump['name'], slug = slugify(official_dump['name']), consumable_type = 'UTIL', duration = official_dump['consumable']['duration_ms'], description = official_dump['consumable']['description'], buy_cost = item['max_offer_unit_price'], sell_cost = item['min_sale_unit_price'])
            if official_dump['consumable']['type'] == 'food':
                i.consumable_type = 'FOOD'
            i.save()
"""

# Test case
item = json.loads(urllib2.urlopen(undead).read())['result']
id = item['data_id']
official_dump = json.loads(urllib2.urlopen(ITEM_DETAIL + str(id)).read())
if official_dump['type'] == 'Consumable':
    i = Item(pk=id, name = official_dump['name'], slug = slugify(official_dump['name']), consumable_type = 'UTIL', duration = official_dump['consumable']['duration_ms'], description = official_dump['consumable']['description'], )
    if official_dump['consumable']['type'] == 'food':
        i.consumable_type = 'FOOD'
    i.save()

