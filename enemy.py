# Class for enemy
class Enemy:
    def __init__(self, name, hp_max, mp_max, attack, defense):
        self.name = name

        self.hp_max = hp_max
        self.mp_max = mp_max
        self.hp = self.hp_max
        self.mp = self.mp_max
        self.attack = attack
        self.defense = defense

    # Displays enemy stats
    def display(self):
        print(self.name)
        print("{:16}".format("HP: ") + "{:>16}".format(str(self.hp) + "/" + str(self.hp_max)))
        print("{:16}".format("MP: ") + "{:>16}".format(str(self.mp) + "/" + str(self.mp_max)))
        print("{:16}".format("ATT: ") + "{:>16}".format(str(self.attack)))
        print("{:16}".format("DEF: ") + "{:>16}".format(str(self.defense)))
