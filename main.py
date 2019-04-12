import player
from time import sleep


player_1 = player.Player("Test1", 1)


while True:
    player_1.calculate_final_stats()
    player_1.calculate_lvl()
    player_1.display()
    player_1.exp += 1
    sleep(0.1)