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


stage = 1  # Stage of the game
phase = 0  # Stores whose turn it is

players = list()
enemies = list()

players.append(Player("Player 1", 1))
enemies.append(Enemy("Dummy", 10, 0, 1, 0))

while True:
    for p in players:
        p.update()
        display()

        print("\n{}'s turn.".format(p.get_name()))

        # Gets player input
        while True:
            p_input = input("Type 'A' to attack.").strip()
            if p_input.lower() == 'a':
                # If more than 1 enemy, asks which enemy to target
                if len(enemies) > 1:
                    while True:
                        p_input = input("Type location of enemy to target.").strip()
                        try:
                            p_input = int(p_input) - 1  # Calculates actual index by subtracting location by 1
                            enemies[p_input].change_hp(-p.get_attack())  # Reduces enemy hp by player attack
                            print("Attacked {}.".format(enemies[p_input].get_name()))
                            break
                        except ValueError:
                            print("Invalid response.")
                else:
                    enemies[0].change_hp(-p.get_attack())  # Reduces enemy hp by player attack
                    print("Attacked {}.".format(enemies[0].get_name()))
                    break
            else:
                print("Invalid response.")

    for e in enemies:
        display()

        print("\n{}'s turn.".format(e.get_name()))

    input()
