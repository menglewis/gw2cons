import json, requests, time
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from django.conf import settings
from ...models import Item

SPIDY_DETAIL = "http://www.gw2spidy.com/api/v0.9/json/item/"

class Command(BaseCommand):
    help = 'Updates the buy and sell price of items with the GW2Spidy API'

    def handle(self, *args, **options):
        items = Item.objects.all()
        for item in items:
            try:
                time.sleep(2) # so we don't hit the API too often
                id = item.id
                spidy_dump = json.loads(requests.get(SPIDY_DETAIL + str(id)).text)['result']
                item.buy_cost = spidy_dump['max_offer_unit_price']
                item.sell_cost = spidy_dump['min_sale_unit_price']
                item.save()
                self.stdout.write("Updated item %s" % id)
            except:
                pass
