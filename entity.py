# Class for any entity; mainly for inheriting
class Entity:
    def __init__(self, name):
        self.name = name

        # Variables to store stats
        self.hp_max = int()
        self.mp_max = int()
        self.hp = int()
        self.mp = int()
        self.attack = int()
        self.defense = int()

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense
