from time import sleep
from random import randint
from player import Player
from enemy import Enemy


# Displays stats of all players and enemies
def display():
    for player in players:
        print("")
        player.display()

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
    # Iterates through players' actions
    for player in players:
        player.update()
        display()

        print("\n{}'s turn.".format(player.get_name()))

        # Gets player's input, keeps trying until input is valid
        while True:
            p_input = input("Type 'A' to attack.").strip()
            
            if p_input.lower() == 'a':
                # If more than 1 enemy, asks which one to target
                if len(enemies) > 1:
                    # Gets player's input, keeps trying until input is valid
                    while True:
                        p_input = input("Type location of enemy to target.").strip()
                        
                        try:
                            p_input = int(p_input) - 1  # Calculates actual index by subtracting location by 1
                            player.attack_entity(enemies[p_input])
                            print("Attacked {} for {} damage.".format(enemies[p_input].get_name(), player.attack_entity_damage(enemies[p_input])))
                            break
                        except ValueError:
                            print("Invalid response.")
                # If just 1 enemy, automatically targets it
                else:
                    player.attack_entity(enemies[0])
                    print("Attacked {} for {} damage.".format(enemies[0].get_name(), player.attack_entity_damage(enemies[0])))
                    break
            else:
                print("Invalid response.")

        check_deaths()

    # Iterates through enemies' actions
    for enemy in enemies:
        display()

        print("\n{}'s turn.".format(enemy.get_name()))

        # If more than 1 player, targets player that would end up with the lowest health if attacked
        if len(players) > 1:            
            target = 0  # Index of target

            # Stores resulting health if first player was attacked
            target_hp = players[0].get_hp() - enemy.attack_entity_damage(players[0])

            # Iterates starting from second player
            for p in range(1, len(players)):
                if players[p].get_hp() - enemy.attack_entity_damage(players[p]) < target_hp:
                    target = p
                    target_hp = players[p].get_hp() - enemy.attack_entity_damage(players[p])
            
            enemy.attack_entity(players[target])
            print("Attacked {} for {} damage.".format(players[target].get_name(), enemy.attack_entity_damage(players[target])))
        # If just 1 player, automatically targets it
        else:
            enemy.attack_entity(players[0])
            print("Attacked {} for {} damage.".format(players[0].get_name(), enemy.attack_entity_damage(players[0])))
    
        check_deaths()
