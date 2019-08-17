from item import Item


# Class for equipment: Player can only have one of each type; adds to stats
class Equipment(Item):
    def __init__(self, name):
        super().__init__(name)
