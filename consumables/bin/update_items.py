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

SPIDY_DETAIL = "http://www.gw2spidy.com/api/v0.9/json/item/"

def main():
    items = Item.objects.all()
    for item in items:
        try:
            id = item['data_id']
            spidy_dump = json.loads(urllib2.urlopen(SPIDY_DETAIL + str(id)).read())['result']
            item.buy_cost = spidy_dump['max_offer_unit_price']
            item.sell_cost = spidy_dump['min_sale_unit_price']
            item.save()
        except:
            pass