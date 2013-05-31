from django.db import models

def convert_cost(cost):
    return '%sg %ss %sc' % (cost / 10000 , (cost % 10000) / 100, cost % 100)

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    buy_cost = models.IntegerField(blank=True, null=True)
    sell_cost = models.IntegerField(blank=True, null=True)
    food = models.BooleanField(default=True)

    def get_buy_cost(self):
        return convert_cost(self.buy_cost)

    def get_sell_cost(self):
        return convert_cost(self.sell_cost)

    def __unicode__(self):
        return self.name

class Stat(models.Model):
    name = models.CharField(max_length=255)
    items = models.ManyToManyField(Item, through="Item_Stat")

    def __unicode__(self):
        return self.name

class Item_Stat(models.Model):
    item = models.ForeignKey(Item)
    stat = models.ForeignKey(Stat)
    magnitude = models.IntegerField()

    def __unicode__(self):
        return '%s: %s %s' % (self.item, self.magnitude, self.stat)

