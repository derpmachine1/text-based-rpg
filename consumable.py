from item import Item


# Class for consumable: Player uses once and gains effect
class Consumable(Item):
    def __init__(self, name, d_hp, d_mp):
        super().__init__(name)

        # Variables to store how item changes stats of player
        self.d_hp = d_hp
        self.d_mp = d_mp

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

    # Displays consumable stats
    def display(self):
        print("| {:16}   {:>48} |".format(self.name, self.stats_str))

    def get_d_hp(self):
        return self.d_hp

    def get_d_mp(self):
        return self.d_mp
