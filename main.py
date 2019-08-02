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

        valid_input = False
        while not valid_input:
            p_input = input("Type 'A' to attack.").strip()
            if p_input.lower() == 'a':
                print("Attacked.")
                valid_input = True
            else:
                print("Invalid response.")

    for e in enemies:
        display()

        print("\n{}'s turn.".format(e.get_name()))

    input()
