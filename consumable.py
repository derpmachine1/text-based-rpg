from item import Item


# Class for consumable: Player uses once and gains effect
class Consumable(Item):
    def __init__(self, name):
        super().__init__(name)
