import player
from time import sleep

player_1 = player.Player("Test1", 1)

stage = 1  # Stage of the game
phase = 0  # Stores whose turn it is

while True:
    player_1.update()
    player_1.display()
    sleep(0.1)
