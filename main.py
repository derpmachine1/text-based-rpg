import player
from time import sleep

player_1 = player.Player("Test1", 1)

while True:
    player_1.update()
    player_1.display()
    sleep(0.1)