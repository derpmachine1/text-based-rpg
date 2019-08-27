from entity import Entity
from random import randint


# Class for player
class Player(Entity):
    def __init__(self, name, difficulty):
        super().__init__(name)

        self.difficulty = difficulty

        # Variables to store base stats
        self.hp_max_base = int(round(20 / self.difficulty))
        self.mp_max_base = int(round(20 / self.difficulty))
        self.hp_base = self.hp_max_base
        self.mp_base = self.mp_max_base
        self.attack_base = int(round(5 / self.difficulty))
        self.defense_base = 0

        # Variables to store final stats; will be used in the future for equipment, status effects, etc
        self.hp_max = self.hp_max_base
        self.mp_max = self.mp_max_base
        self.hp = self.hp_base
        self.mp = self.mp_base
        self.attack = self.attack_base
        self.defense = self.defense_base

        self.exp = 0
        self.exp_req = 0
        self.lvl = 1

        self.equipment = list()  # Stores equipment
        self.items = list()  # Stores all other items

    # Updates everything about the player
    def update(self):
        self.calculate_lvl()
        self.calculate_final_stats()

    # Adds modifiers to base stats
    def calculate_final_stats(self):
        self.hp_max = self.hp_max_base
        self.mp_max = self.mp_max_base
        self.hp = self.hp_base
        self.mp = self.mp_base
        self.attack = self.attack_base
        self.defense = self.defense_base

        for equipment in self.equipment:
            self.hp_max += equipment.get_d_hp()
            self.mp_max += equipment.get_d_mp()
            self.hp += equipment.get_d_hp()
            self.mp += equipment.get_d_mp()
            self.attack += equipment.get_d_attack()
            self.defense += equipment.get_d_defense()

    # Calculates exp required to next level and handles level ups
    def calculate_lvl(self):
        self.exp_req = self.lvl * 10

        if self.exp >= self.exp_req:
            self.lvl += 1
            self.exp -= self.exp_req

            # Increases base stats
            x = randint(4, 8)
            self.hp_max_base += x
            self.hp_base += x
            x = randint(4, 8)
            self.mp_max_base += x
            self.mp_base += x
            self.attack_base += randint(1, 2)

            self.exp_req = self.lvl * 10

    # Displays player stats
    def display(self):
        print("| {:32} | {:8}{:>24} |".format(self.name, "LVL " + str(self.lvl) + ":", str(self.exp) + "/" + str(self.exp_req)))
        print("| {:8}{:>24} | {:8}{:>24} |".format("HP:", str(self.hp) + "/" + str(self.hp_max), "MP:", str(self.mp) + "/" + str(self.mp_max)))
        print("| {:8}{:>24} | {:8}{:>24} |".format("ATT:", str(self.attack), "DEF:", str(self.defense)))

    def get_lvl(self):
        return self.lvl

    def get_equipment(self):
        return self.equipment

    def get_items(self):
        return self.items

    def change_hp(self, d_hp):
        self.hp_base += d_hp
        self.hp += d_hp

    def change_mp(self, d_mp):
        self.mp_base = d_mp
        self.mp += d_mp

    def change_exp(self, d_exp):
        self.exp += d_exp

    def add_equipment(self, equipment):
        # Tries to remove any other held equipment of the same type
        for e in range(len(self.equipment)):
            if equipment.get_type() == self.equipment[e].get_type():
                del self.equipment[e]

        self.equipment.append(equipment)

    def remove_equipment(self, e):
        del self.equipment[e]

    # Checks if player already has equipment of a certain type; returns index of duplicate or -1
    def check_equipment_type(self, equip_type):
        # Tries to remove any other held equipment of the same type
        for e in range(len(self.equipment)):
            if equip_type == self.equipment[e].get_type():
                return e

        return -1

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, i):
        del self.items[i]

    def use_item(self, i):
        self.items[i].use(self)
        self.remove_item(i)
