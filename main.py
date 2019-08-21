from time import sleep
from random import randint
from os import listdir
from player import Player
from enemy import Enemy
from equipment import Equipment


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
            sleep(delay)

            del players[p]

    for e in range(len(enemies)):
        if enemies[e].is_dead():
            print("{} was defeated.".format(enemies[e].get_name()))
            sleep(delay)

            for player in players:
                # Experience gain
                player.change_exp(enemies[e].get_exp())
                print("{} gained {} experience.".format(player.get_name(), enemies[e].get_exp()))
                sleep(delay)

                # Rolls for items
                with open("enemy_data/{}.txt".format(enemies[e].get_name().replace(' ', '_'))) as f_in:
                    enemy = f_in.readlines()
                    if len(enemy) > 1:  # Item drops of enemy are stored after first line of enemy file
                        for item_drop in enemy[1:]:
                            if randint(1, 100) <= int(item_drop.split()[1]):
                                with open("item_data/{}.txt".format(item_drop.split()[0])) as f_in2:
                                    # For equipment items
                                    if f_in2.readline().strip() == "equipment":
                                        new_item = f_in2.readline().split()

                                        # If player does not already have an equipment item of the same type
                                        if player.check_equipment_type(new_item[1]) == -1:
                                            potential_equip = Equipment(new_item[0], new_item[1], int(new_item[2]), int(new_item[3]), int(new_item[4]), int(new_item[5]))
                                            print("{} found {}.".format(player.get_name(), potential_equip.get_name()))
                                            sleep(delay)
                                            potential_equip.display()
                                            sleep(delay)

                                            while True:
                                                p_input = input("'Y' to take equipment, 'N' to discard equipment.")

                                                if p_input.lower() == 'y':
                                                    player.add_equipment(potential_equip)
                                                    print("{} took {}.".format(player.get_name(), player.get_equipment()[-1].get_name()))
                                                    sleep(delay)
                                                    player.get_equipment()[-1].display()
                                                    sleep(delay)
                                                    break

                                                elif p_input.lower() == 'n':
                                                    print("{} discarded {}.".format(player.get_name(), potential_equip.get_name()))
                                                    sleep(delay)
                                                    break

                                                else:
                                                    print("Invalid response: Expected 'Y' or 'N'.")
                                                    sleep(delay)

                                        # Else, asks player whether to replace it or not
                                        else:
                                            potential_equip = Equipment(new_item[0], new_item[1], int(new_item[2]), int(new_item[3]), int(new_item[4]), int(new_item[5]))
                                            print("{} found {} but already has a(n) {}.".format(player.get_name(), potential_equip.get_name(), potential_equip.get_type()))
                                            sleep(delay)
                                            print("Old:")
                                            sleep(delay)
                                            player.get_equipment()[player.check_equipment_type(new_item[1])].display()
                                            sleep(delay)
                                            print("New:")
                                            sleep(delay)
                                            potential_equip.display()
                                            sleep(delay)

                                            while True:
                                                p_input = input("'Y' to take new equipment, 'N' to keep old equipment.")

                                                if p_input.lower() == 'y':
                                                    player.add_equipment(potential_equip)
                                                    print("{} discarded {} and took {}.".format(player.get_name(), player.get_equipment()[player.check_equipment_type(new_item[1])].get_name(), player.get_equipment()[-1].get_name()))
                                                    sleep(delay)
                                                    player.get_equipment()[-1].display()
                                                    sleep(delay)
                                                    break

                                                elif p_input.lower() == 'n':
                                                    print("{} discarded {}.".format(player.get_name(), potential_equip.get_name()))
                                                    sleep(delay)
                                                    break

                                                else:
                                                    print("Invalid response: Expected 'Y' or 'N'.")
                                                    sleep(delay)

            del enemies[e]


delay = 0.5  # Time delay between text

total_stages = len(listdir('enemy_data'))  # Total number of stages built into the game
stage = 1  # Stage of the game
encounters = 0  # Number of enemy encounters in current level thus far
enemy_data = list()  # Stores data of all possible enemies on current level

players = list()
enemies = list()

players.append(Player("Player1", 1))
# players.append(Player("Player2", 1))


# Setup for first stage
enemy_data = list()
with open("stage_data/1.txt", 'r') as f_in:
    for enemy in f_in.readlines():
        with open("enemy_data/{}.txt".format(enemy.split()[0])) as f_in2:
            new_enemy = f_in2.readline().split()
            for i in range(int(enemy.split()[1])):
                enemy_data.append(new_enemy)

while True:
    # If finished level (4 normal encounters + boss encounter)
    if encounters == 5:
        print("Floor {} cleared.".format(stage))
        sleep(delay)

        # Activates endless mode if finished all programmed stages
        if stage == total_stages or stage == 0:
            stage = 0
            encounters = 0

            print("Entering endless floor.")
            sleep(delay)

            # Randomly generates enemies scaled to level
            average_lvl = sum([player.get_lvl() for player in players]) // len(players)
            enemy_data = list()
            enemy_data.append(["Boss",
                               average_lvl * 10 + randint(30, 50),
                               average_lvl * 10 + randint(30, 50),
                               average_lvl * 1 + randint(8, 12),
                               average_lvl * 1 + randint(4, 6),
                               average_lvl * 2])
            for i in range(10):
                enemy_data.append(["Enemy",
                                   average_lvl * 5 + randint(15, 25),
                                   average_lvl * 5 + randint(15, 25),
                                   average_lvl * 1 + randint(4, 6),
                                   average_lvl * 1 + randint(2, 3),
                                   average_lvl])

        else:
            stage += 1
            encounters = 0

            print("Entering floor {}.".format(stage))
            sleep(delay)

            # Reads and stores enemy data for new level
            enemy_data = list()
            with open("stage_data/{}.txt".format(stage), 'r') as f_in:
                for enemy in f_in.readlines():
                    with open("enemy_data/{}.txt".format(enemy.split()[0])) as f_in2:
                        new_enemy = f_in2.readline().split()
                        for i in range(int(enemy.split()[1])):
                            enemy_data.append(new_enemy)

    # If no players left, lose
    if len(players) == 0:
        break

    # If no enemies left, create more enemies
    if len(enemies) == 0:
        # Spawns boss after 4 encounters
        if encounters == 4:
            new_enemy = enemy_data[0]
            enemies.append(Enemy(new_enemy[0].replace('_', ' '), int(new_enemy[1]), int(new_enemy[2]), int(new_enemy[3]), int(new_enemy[4]), int(new_enemy[5])))
            print("Encountered floor boss, {}.".format(enemies[-1].get_name()))
            sleep(delay)
        else:
            new_enemy = enemy_data[randint(1, len(enemy_data) - 1)]
            enemies.append(Enemy(new_enemy[0].replace('_', ' '), int(new_enemy[1]), int(new_enemy[2]), int(new_enemy[3]), int(new_enemy[4]), int(new_enemy[5])))
            print("Encountered {}.".format(enemies[-1].get_name()))
            sleep(delay)

        encounters += 1

    # Iterates through players' actions
    for player in players:
        player.update()
        display()

        print("\n{}'s turn.".format(player.get_name()))
        sleep(delay)

        # Gets player's input, keeps trying until input is valid
        while True:
            p_input = input("'A' to attack, 'E' to check equipment.").strip()
            
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
                            print("{} attacked {} for {} damage.".format(player.get_name(), enemies[p_input].get_name(), player.attack_entity_damage(enemies[p_input])))
                            sleep(delay)
                            break
                        except ValueError:
                            print("Invalid response: Expected whole number.")
                            sleep(delay)
                        except IndexError:
                            print("Invalid response: No enemy at inputted location.")
                            sleep(delay)
                    break
                # If just 1 enemy, automatically targets it
                else:
                    player.attack_entity(enemies[0])
                    print("{} attacked {} for {} damage.".format(player.get_name(), enemies[0].get_name(), player.attack_entity_damage(enemies[0])))
                    sleep(delay)
                    break

            elif p_input.lower() == 'e':
                if len(player.get_equipment()) == 0:
                    print("{} has no equipment.".format(player.get_name()))
                    sleep(delay)
                else:
                    print("{} has:".format(player.get_name()))
                    sleep(delay)
                    for equipment in player.get_equipment():
                        equipment.display()
                        sleep(delay)

            else:
                print("Invalid response: Expected 'A' or 'E'.")
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

print("Game over.")
