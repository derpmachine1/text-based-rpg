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

    sleep(delay)
    

def check_deaths():
    for p in range(len(players)):
        if players[p].is_dead():
            print("{} was defeated.".format(players[p].get_name()))
            del players[p]
            sleep(delay)

    for e in range(len(enemies)):
        if enemies[e].is_dead():
            print("{} was defeated.".format(enemies[e].get_name()))
            del enemies[e]
            sleep(delay)


delay = 1  # Time delay between text

level = 1  # Stage of the game
encounters = 0  # Number of enemy encounters in current level thus far
enemy_data = list()  # Stores data of all possible enemies on current level

players = list()
enemies = list()

players.append(Player("Player1", 1))
# players.append(Player("Player2", 1))


# Setup for first level
print("Entered level 1.")
sleep(delay)
with open("enemy_data/1.txt", 'r') as f_in:
    enemy_data = [enemy.split() for enemy in f_in.readlines()]

while True:
    # If finished level
    if encounters == 10:
        print("Finished level {}.".format(level))
        sleep(delay)

        level += 1
        encounters = 0

        print("Entered level {}.".format(level))
        sleep(delay)

        # Reads and stores enemy data for new level
        with open("enemy_data/{}.txt".format(level), 'r') as f_in:
            enemy_data = [enemy.split() for enemy in f_in.readlines()]

    # If no enemies left, create more enemies
    if len(enemies) == 0:
        encounters += 1

        new_enemy = enemy_data[randint(0, len(enemy_data) - 1)]
        enemies.append(Enemy(new_enemy[0], int(new_enemy[1]), int(new_enemy[2]), int(new_enemy[3]), int(new_enemy[4])))
        print("Encountered {}.".format(new_enemy[0]))
        sleep(delay)

    # Iterates through players' actions
    for player in players:
        player.update()
        display()

        print("\n{}'s turn.".format(player.get_name()))
        sleep(delay)

        # Gets player's input, keeps trying until input is valid
        while True:
            p_input = input("Type 'A' to attack.").strip()
            
            if p_input.lower() == 'a':
                # If more than 1 enemy, asks which one to target
                if len(enemies) > 1:
                    # Gets player's input, keeps trying until input is valid
                    while True:
                        p_input = input("Type location of enemy to target.").strip()
                        sleep(delay)
                        
                        try:
                            p_input = int(p_input) - 1  # Calculates actual index by subtracting location by 1
                            player.attack_entity(enemies[p_input])
                            print("Attacked {} for {} damage.".format(enemies[p_input].get_name(), player.attack_entity_damage(enemies[p_input])))
                            sleep(delay)
                            break
                        except ValueError:
                            print("Invalid response.")
                            sleep(delay)
                        except IndexError:
                            print("Invalid response.")
                            sleep(delay)
                    break
                # If just 1 enemy, automatically targets it
                else:
                    player.attack_entity(enemies[0])
                    print("Attacked {} for {} damage.".format(enemies[0].get_name(), player.attack_entity_damage(enemies[0])))
                    sleep(delay)
                    break
            else:
                print("Invalid response.")
                sleep(delay)

        check_deaths()

    # Iterates through enemies' actions
    for enemy in enemies:
        display()

        print("\n{}'s turn.".format(enemy.get_name()))
        sleep(delay)

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
            sleep(delay)
        # If just 1 player, automatically targets it
        else:
            enemy.attack_entity(players[0])
            print("Attacked {} for {} damage.".format(players[0].get_name(), enemy.attack_entity_damage(players[0])))
            sleep(delay)
    
        check_deaths()
