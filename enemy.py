from entity import Entity


# Class for enemy
class Enemy(Entity):
    def __init__(self, name, hp_max, mp_max, attack, defense, weight, exp):
        super().__init__(name)

        # Variables to store stats
        self.hp_max = hp_max
        self.mp_max = mp_max
        self.hp = self.hp_max
        self.mp = self.mp_max
        self.attack = attack
        self.defense = defense

        # Enemy-specific variables
        self.weight = weight  # Modifies how often it appears
        self.exp = exp  # Exp given when killed

    # Displays enemy stats; accepts index of enemy to allow function to display location
    def display(self, index):
        print("| {:32} | {:32} |".format(self.name, "LOCATION " + str(index + 1)))
        print("| {:8}{:>24} | {:8}{:>24} |".format("HP:", str(self.hp) + "/" + str(self.hp_max), "MP:", str(self.mp) + "/" + str(self.mp_max)))
        print("| {:8}{:>24} | {:8}{:>24} |".format("ATT:", str(self.attack), "DEF:", str(self.defense)))

    def get_weight(self):
        return self.weight

    def get_exp(self):
        return self.exp
