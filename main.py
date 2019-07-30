from player import Player
from enemy import Enemy
from time import sleep

stage = 1  # Stage of the game
phase = 0  # Stores whose turn it is

players = list()
enemies = list()

players.append(Player("Player 1", 1))
enemies.append(Enemy("Dummy", 10, 0, 1, 0))

while True:
    for player in players:
        player.update()
        print("")
        player.display()

    for enemy in enemies:
        print("")
        enemy.display()

    input()
