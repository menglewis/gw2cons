import json
import urllib2

from django.template.defaultfilters import slugify

from .models import Item

CONSUMABLES_API = "http://www.gw2spidy.com/api/v0.9/json/all-items/3"

ITEM_DETAIL = "https://api.guildwars2.com/v1/item_details.json?item_id="

undead = "http://www.gw2spidy.com/api/v0.9/json/item/8878"

items = json.loads(urllib2.urlopen(CONSUMABLES_API).read())['results']

for item in items:
    if (item['sub_type_id'] == 2):
        id = item['data_id']
        official_dump = json.loads(urllib2.urlopen(ITEM_DETAIL + str(apple_pie)).read())
    i = Item(pk=id, name = official_dump['name'], slug = slugify(official_dump['name']), duration = official_dump['consumable']['duration_ms'], consumable_type = 'FOOD', description = official_dump['consumable']['description'])

# need type 3 subtype 2

item = json.loads(urllib2.urlopen(ITEM_DETAIL + str(apple_pie)).read())

# name
item['name']

# level
item['level']

# Item type
item['consumable']['type']

# Duration
item['consumable']['duration_ms']

# stats
item['consumable']['description']
