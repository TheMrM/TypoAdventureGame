import random
import ascii
from characters import *
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Spider fight with sword
def spider_fight_sword(player_stats, spider_stats, delay_speed):
    while True:
        slow_print("Type 'roll' to roll the dice that will determine your next action in the battle: ")
        roll = input()
        dice = random.randint(1, 6)
        if dice <= 2:
            slow_print("You have rolled a low dice. You have missed the spider. The spider has attacked you and you have lost 1 life.")
            player_stats['life'] -= 1
            slow_print(f"You have {player_stats['life']} lives left.")
        elif dice <= 5:
            slow_print("You have rolled a medium dice. You have hit the spider. The spider has attacked you and you have lost 1 life.")
            player_stats['life'] -= 1
            spider_stats['life'] -= 2
            slow_print(f"The spider has {spider_stats['life']} lives left. You have {player_stats['life']} lives left.")
        elif dice == 6:
            slow_print("You have rolled a high dice. You sword has cut his legs. And with a killer blow you kill him in his web.")
            slow_print(f"You have {player_stats['life']} lives left.")
            slow_print(f"You have vanquished the spider. The dragon awaits.\n{ascii.map_forest_1}")
            from dragons import dragon
            dragon()
            return

        if player_stats['life'] <= 0:
            slow_print("You have lost all your lives. You have failed to vanquish the spider.")
            slow_print(f"Game OVER!\n{ascii.skull}")
            break
        elif spider_stats['life'] <= 0:
            slow_print(f"You have vanquished the spider. The dragon awaits.\n{ascii.map_forest_1}")
            from characters import dragon_stats
            from dragons import dragon
            dragon()
            return

# Spider fight with bow
def spider_fight_bow(player_stats, spider_stats, delay_speed):
    while True:
        slow_print("Type 'roll' to roll the dice that will determine your next action in the battle: ")
        roll = input()
        dice = random.randint(1, 6)
        if dice <= 2:
            slow_print("You have rolled a low dice. Your arrow has not found its way. The spider has attacked you and you have lost 1 life.")
            player_stats['life'] -= 1
            slow_print(f"You have {player_stats['life']} lives left.")
        elif dice <= 5:
            slow_print("You have rolled a medium dice. Your arrow has found its way. The spider has attacked you and you have lost 1 life.")
            player_stats['life'] -= 1
            spider_stats['life'] -= 2
            slow_print(f"The spider has {spider_stats['life']} lives left. You have {player_stats['life']} lives left.")
        elif dice == 6:
            slow_print("You have rolled a high dice. Your arrow has found its way. And with a critical hit you kill him in his web.")
            slow_print(f"You have {player_stats['life']} lives left.")
            slow_print(f"You have vanquished the spider. The dragon awaits.\n{ascii.map_forest_1}")
            from dragons import dragon
            dragon()
            return

        if player_stats['life'] <= 0:
            slow_print("You have lost all your lives. You have failed to vanquish the spider.")
            slow_print(f"Game OVER!\n{ascii.skull}")
            from main import beginning, delay_speed
            beginning(delay_speed)
            break
        elif spider_stats['life'] <= 0:
            slow_print(f"You have vanquished the spider. The dragon awaits.\n{ascii.map_forest_1}")
            from dragons import dragon
            dragon()
            return