from item import Item


# Class for equipment: Player can only have one of each type; adds to stats
class Equipment(Item):
    def __init__(self, name, equip_type, d_hp, d_mp, d_attack, d_defense):
        super().__init__(name)
        self.equip_type = equip_type

        # Variables to store how item changes stats of player
        self.d_hp = d_hp
        self.d_mp = d_mp
        self.d_attack = d_attack
        self.d_defense = d_defense

        # String that is printed when the equipment is displayed
        self.stats_str = str()
        if self.d_hp > 0:
            self.stats_str += "[+{} HP] ".format(self.d_hp)
        elif self.d_hp > 0:
            self.stats_str += "[-{} HP] ".format(-self.d_hp)
        if self.d_mp > 0:
            self.stats_str += "[+{} MP] ".format(self.d_mp)
        elif self.d_mp > 0:
            self.stats_str += "[-{} MP] ".format(-self.d_mp)
        if self.d_attack > 0:
            self.stats_str += "[+{} ATT] ".format(self.d_attack)
        elif self.d_attack > 0:
            self.stats_str += "[-{} ATT] ".format(-self.d_attack)
        if self.d_defense > 0:
            self.stats_str += "[+{} DEF] ".format(self.d_defense)
        elif self.d_defense > 0:
            self.stats_str += "[-{} DEF] ".format(-self.d_defense)
        self.stats_str = self.stats_str.rstrip(' ')

    # Displays equipment stats
    def display(self):
        print("| {:16}   {:>48} |".format(self.name + ' (' + self.equip_type + ')', self.stats_str))

    def get_type(self):
        return self.equip_type

    def get_d_hp(self):
        return self.d_hp

    def get_d_mp(self):
        return self.d_mp

    def get_d_attack(self):
        return self.d_attack

    def get_d_defense(self):
        return self.d_defense
