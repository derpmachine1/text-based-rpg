# Class for any item; mainly for inheriting
class Item:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
