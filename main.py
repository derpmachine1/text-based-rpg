from player import Player
from enemy import Enemy
from time import sleep


def display():
    for p in players:
        print("")
        p.display()

    for e in range(len(enemies)):
        print("")
        enemies[e].display(e)


def check_deaths():
    for p in range(len(players)):
        if players[p].is_dead():
            print("{} was defeated.".format(players[p].get_name()))
            del players[p]

    for e in range(len(enemies)):
        if enemies[e].is_dead():
            print("{} was defeated.".format(enemies[e].get_name()))
            del enemies[e]


stage = 1  # Stage of the game

players = list()
enemies = list()

players.append(Player("Player 1", 1))
enemies.append(Enemy("Dummy", 25, 0, 5, 0))

while True:
    # Iterate through players' actions
    for p in players:
        p.update()
        display()

        print("\n{}'s turn.".format(p.get_name()))

        # Gets player input
        while True:
            p_input = input("Type 'A' to attack.").strip()

            if p_input.lower() == 'a':
                # If more than 1 enemy, asks which one to target
                if len(enemies) > 1:
                    while True:
                        p_input = input("Type location of enemy to target.").strip()
                        try:
                            p_input = int(p_input) - 1  # Calculates actual index by subtracting location by 1
                            p.attack_entity(enemies[p_input])
                            print("Attacked {} for {} damage.".format(enemies[p_input].get_name(), p.attack_entity_damage(enemies[p_input])))
                            break
                        except ValueError:
                            print("Invalid response.")
                else:
                    p.attack_entity(enemies[0])
                    print("Attacked {} for {} damage.".format(enemies[0].get_name(), p.attack_entity_damage(enemies[0])))
                    break
            else:
                print("Invalid response.")

        check_deaths()

    # Iterate through enemies' actions
    for e in enemies:
        display()

        print("\n{}'s turn.".format(e.get_name()))

        check_deaths()
