#  https://www.codewars.com/kata/shop-inventory-manager
converted_items = False

class Item:
    min_quality, max_quality = 0, 50

    def __init__(self,name, sell_in, quality, degrade_multiplier=1):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.degrade_value = degrade_multiplier
        self.sell_in_days_dropped = False
        self.increase_quality = False
        self.enforce_degradation()

    def update_q(self):
        self.sell_in -= 1
        self.enforce_degradation()

        self.quality += self.degrade_value if self.increase_quality else -self.degrade_value
        self.enforce_quality_limits()

    def enforce_quality_limits(self):
        if self.quality < self.min_quality:
            self.quality = self.min_quality

    def enforce_degradation(self):
        if self.sell_in < 0 and not self.sell_in_days_dropped:
            # Quality degrades twice as fast
            self.degrade_value *= 2
            self.sell_in_days_dropped = True


class ConjuredItem(Item):
    """ Conjured Items degrade twice as fast """
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
        self.degrade_value *= 2


class AgedItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
        self.increase_quality = True
        self.orig_quality = quality

    def update_q(self):
        if self.quality > 50:
            # Quality should not be altered
            self.sell_in -= 1
        else:
            Item.update_q(self)

    def enforce_quality_limits(self):
        """ Cannot increase beyond 50 """
        if self.orig_quality <= 50:
            if self.quality >= 50:
                self.quality = 50

    def enforce_degradation(self):
        pass


class BackstagePass(AgedItem):
    """ Backstage Passes also increase in value, although they have different degradation multipliers """
    def __init__(self, name, sell_in, quality):
        self.increased_by_two = False
        self.increased_by_three = False
        AgedItem.__init__(self, name, sell_in, quality)

    def enforce_degradation(self):
        if not self.increased_by_two and  5 < self.sell_in <= 10:
            self.degrade_value = 2
            self.increased_by_two = True
        elif not self.increased_by_three and 0 < self.sell_in <= 5:
            self.degrade_value = 3
            self.increased_by_three = True
        elif 0 >= self.sell_in:
            self.degrade_value = 0
            self.quality = 0


class LegendaryItem(Item):
    def update_q(self, to_increase=False):
        # Legendary items dont have their stuff altered
        pass



items=[]

items+=[Item('+5 Dexterity Vest', 10, 20)]
items+=[Item('Aged Brie', 2, 0)]
items+=[Item('Elixir of the Mongoose', 5, 7)]
items+=[Item('Sulfuras, Hand of Ragnaros', 0, 80)]
items+=[Item('Backstage passes to a TAFKAL80ETC concert', 15, 20)]
items+=[Item('Conjured Mana Cake', 3, 6)]
items += [Item("Vety Aged Brie", 10, 40)]

def convert_items(items):
    """ This function takes a list of items and modifies them to the applicable subclass """
    for idx in range(len(items)):
        item_name, item_sell_in, item_quality = items[idx].name, items[idx].sell_in, items[idx].quality,
        comp_name = item_name.lower()  # the name with which we compare by

        new_item = items[idx]
        if 'aged brie' in comp_name:
            new_item = AgedItem(item_name, item_sell_in, item_quality)
        elif 'sulfuras' in comp_name:
            new_item = LegendaryItem(item_name, item_sell_in, item_quality)
        elif 'conjured' in comp_name:
            new_item = ConjuredItem(item_name, item_sell_in, item_quality)
        elif 'backstage passes' in comp_name:
            new_item = BackstagePass(item_name, item_sell_in, item_quality)
        items[idx] = new_item

    return items


def update_quality():
    """
    Updates the quality of each item
    """
    global items, converted_items
    if not converted_items:
        items = convert_items(items)
        converted_items = True
    for item in items:
        item.update_q()
