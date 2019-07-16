from player import Player
from enemy import Enemy
from time import sleep

stage = 1  # Stage of the game
phase = 0  # Stores whose turn it is

players = list()
enemies = list()

players.append(Player("Player 1", 1))

while True:
    for player in players:
        player.update()
        player.display()
        print("")

    for enemy in enemies:
        enemy.display()
        print("")

    input()
