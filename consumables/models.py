from django.db import models
from django.template.defaultfilters import slugify

def convert_cost(cost):
    if (cost is None):
        return '0'
    elif (cost > 9999):
        return '%sg %ss %sc' % (cost / 10000 , (cost % 10000) / 100, cost % 100)
    elif (cost > 99):
        return '%ss %sc' % (cost / 100, cost % 100)
    else:
        return '%sc' % cost

class Item(models.Model):

    CONSUMABLE_TYPES = (
        ('FOOD', 'Food'),
        ('UTIL', 'Utility'),
    )

    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    buy_cost = models.IntegerField(blank=True, null=True)
    sell_cost = models.IntegerField(blank=True, null=True)
    consumable_type = models.CharField(max_length=4, choices = CONSUMABLE_TYPES, default="FOOD")
    slug = models.SlugField(max_length=255, blank=True, default='')

    description = models.TextField()

    def get_buy_cost(self):
        return convert_cost(self.buy_cost)

    def get_sell_cost(self):
        return convert_cost(self.sell_cost)

    def __unicode__(self):
        return self.name

    def __save__(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ("consumables:detail", (), {"slug": self.slug})

class Stat(models.Model):
    name = models.CharField(max_length=255)
    items = models.ManyToManyField(Item, through="Item_Stat")

    def __unicode__(self):
        return self.name

class Item_Stat(models.Model):
    item = models.ForeignKey(Item)
    stat = models.ForeignKey(Stat)
    magnitude = models.IntegerField()
    order_number = models.IntegerField()

    def __unicode__(self):
        return '%s: %s %s' % (self.item, self.magnitude, self.stat)

