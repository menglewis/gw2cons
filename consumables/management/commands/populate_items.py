import json, requests, time
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from django.conf import settings
from ...models import Item

CONSUMABLES_API = "http://www.gw2spidy.com/api/v0.9/json/all-items/3"
DETAIL_API = "https://api.guildwars2.com/v1/item_details.json?item_id="

class Command(BaseCommand):
    help = 'Populates the DB with items from the API'

    def handle(self, *args, **options):
        items = json.loads(requests.get(CONSUMABLES_API).text)['results']
        for item in items:
            try:
                time.sleep(2) # so we don't hit the API too often
                id = item['data_id']
                official_dump = json.loads(requests.get(DETAIL_API + str(id)).text)
                if official_dump['type'] == 'Consumable':
                    i = Item(pk=id, name = official_dump['name'], slug = slugify(official_dump['name']), consumable_type = official_dump['consumable']['type'], duration = official_dump['consumable']['duration_ms'], description = official_dump['consumable']['description'], buy_cost = item['max_offer_unit_price'], sell_cost = item['min_sale_unit_price'])
                    i.save()
                    self.stdout.write("Created item %s" % id)
            except:
                pass
