from player import Player
from enemy import Enemy
from time import sleep


def display():
    for player in players:
        print("")
        player.display()

    for enemy in enemies:
        print("")
        enemy.display()


stage = 1  # Stage of the game
phase = 0  # Stores whose turn it is

players = list()
enemies = list()

players.append(Player("Player 1", 1))
enemies.append(Enemy("Dummy", 10, 0, 1, 0))

while True:
    for player in players:
        player.update()
        display()

        print("\n{}'s turn.".format(player.get_name()))

        valid_input = False
        while not valid_input:
            player_input = input("Type 'A' to attack.").strip()
            if player_input.lower() == 'a':
                print("Attacked.")
                valid_input = True
            else:
                print("Invalid response.")

    for enemy in enemies:
        display()

        print("\n{}'s turn.".format(enemy.get_name()))

    input()
