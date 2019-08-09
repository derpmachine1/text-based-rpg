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

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def change_hp(self, d_hp):
        self.hp += d_hp

    def change_mp(self, d_mp):
        self.mp += d_mp

    # Attacks another entity, factoring own attack and enemy defense
    def attack_entity(self, entity):
        entity.change_hp(-max(0, self.attack - entity.get_defense()))

    # Simulates attacking another entity and returns damage that would be done
    def attack_entity_damage(self, entity):
        return max(0, self.attack - entity.get_defense())
