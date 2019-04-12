from random import randint

# Class for player
class Player:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

        self.hp_max_base = int(round(100 * self.difficulty))
        self.mp_max_base = int(round(100 * self.difficulty))
        self.hp_base = self.hp_max_base
        self.mp_base = self.mp_max_base
        self.attack_base = int(round(10 * self.difficulty))
        self.defense_base = 0

        self.hp_max = self.hp_max_base
        self.mp_max = self.mp_max_base
        self.hp = self.hp_base
        self.mp = self.mp_base
        self.attack = self.attack_base
        self.defense = self.defense_base

        self.exp = 0
        self.exp_req = 0
        self.lvl = 1

    # Adds modifiers to base stats
    def calculate_final_stats(self):
        self.hp_max = self.hp_max_base
        self.mp_max = self.mp_max_base
        self.hp = self.hp_base
        self.mp = self.mp_base
        self.attack = self.attack_base
        self.defense = self.defense_base

    # Calculates exp required to next level and handles level ups
    def calculate_lvl(self):
        self.exp_req = self.lvl * 10

        if self.exp >= self.exp_req:
            self.lvl += 1
            self.exp -= self.exp_req

            self.hp_max_base += randint(5, 15)
            self.mp_max_base += randint(5, 15)
            self.attack_base += randint(1, 3)

            self.exp_req = self.lvl * 10

    # Displays player stats
    def display(self):
        print(self.name)
        print("{:16}".format("LVL " + str(self.lvl) + ":") + "{:>16}".format(str(self.exp) + "/" + str(self.exp_req)))
        print("{:16}".format("HP: ") + "{:>16}".format(str(self.hp) + "/" + str(self.hp_max)))
        print("{:16}".format("MP: ") + "{:>16}".format(str(self.mp) + "/" + str(self.mp_max)))
        print("{:16}".format("ATT: ") + "{:>16}".format(str(self.attack)))
        print("{:16}".format("DEF: ") + "{:>16}".format(str(self.defense)))
