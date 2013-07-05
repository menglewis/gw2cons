import json, urllib2
from django.template.defaultfilters import slugify
from django.conf import settings

settings.configure()
settings.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'cons.db',
    }
}

from ..models import Item

CONSUMABLES_API = "http://www.gw2spidy.com/api/v0.9/json/all-items/3"
DETAIL_API = "https://api.guildwars2.com/v1/item_details.json?item_id="

def main():
    items = json.loads(urllib2.urlopen(CONSUMABLES_API).read())['results']
    for item in items:
        try:
            id = item['data_id']
            official_dump = json.loads(urllib2.urlopen(DETAIL_API + str(id)).read())
            if official_dump['type'] == 'Consumable':
                i = Item(pk=id, name = official_dump['name'], slug = slugify(official_dump['name']), consumable_type = 'UTIL', duration = official_dump['consumable']['duration_ms'], description = official_dump['consumable']['description'], buy_cost = item['max_offer_unit_price'], sell_cost = item['min_sale_unit_price'])
                if official_dump['consumable']['type'] == 'Food':
                    i.consumable_type = 'FOOD'
                i.save()
        except:
            pass
        
if __name__ == "__main__":
    main()

