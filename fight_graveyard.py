import random
import ascii
from characters import *
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

#Code that defines the ghost fight with sword
def ghost_fight_sword(player_stats, ghost_stats):
    while True:
        slow_print("Type 'roll' to roll the dice that will determine your next action in the battle: ")
        roll = input()
        dice = random.randint(1, 6)
        if dice <= 2:
            slow_print("You have rolled a low dice. You have missed the ghost. The ghost has attacked you and you have lost 1 life.")
            player_stats['life'] -= 1
            slow_print(f"You have {player_stats['life']} lives left.")
        elif dice <= 5:
            slow_print("You have rolled a medium dice. You have hit the ghost. The ghost has attacked you and you have lost 1 life.")
            player_stats['life'] -= 1
            ghost_stats['life'] -= 2
            slow_print(f"The ghost has {ghost_stats['life']} lives left. You have {player_stats['life']} lives left.")
        elif dice == 6:
            slow_print("You have rolled a high dice. You have sliced through the ghost, and it disappears into the ether.")
            slow_print(f"You have {player_stats['life']} lives left.")
            slow_print(f"You have vanquished the ghost. The dragon awaits.\n{ascii.map_cemetery_1}")
            from characters import dragon
            dragon()
            return
        
        if  player_stats['life'] <= 0:
            slow_print("You have lost all your lives. You have failed to vanquish the ghost.")
            slow_print(f"Game OVER!\n{ascii.skull}")
            from main import beginning
            beginning()
            break
        elif ghost_stats['life'] <= 0:
            slow_print(f"You have vanquished the ghost. The dragon awaits.\n{ascii.map_cemetery_1}")
            from characters import dragon
            dragon()
            return

#Code that defines the ghost fight with bow            
def ghost_fight_bow(player_stats, ghost_stats):
    while True:
        slow_print("Type 'roll' to roll the dice that will determine your next action in the battle: ")
        roll = input()
        dice = random.randint(1, 6)
        if dice <= 2:
            slow_print("You have rolled a low dice. You have missed the ghost. The ghost has attacked you and you have lost 1 life.")
            player_stats['life'] -= 1
            slow_print(f"You have {player_stats['life']} lives left.")
        elif dice <= 5:
            slow_print("You have rolled a medium dice. Your arrow has hit the ghost. The ghost has attacked you and you have lost 1 life.")
            player_stats['life'] -= 1
            ghost_stats['life'] -= 2
            slow_print(f"The ghost has {ghost_stats['life']} lives left. You have {player_stats['life']} lives left.")
        elif dice == 6:
            slow_print("You have rolled a high dice. You'r arrow found its way. And with a critical hit you kill him it nears is grave.")                
            slow_print(f"You have {player_stats['life']} lives left.")
            slow_print(f"You have vanquished the ghost. The dragon awaits.\n{ascii.map_cemetery_1}")
            from dragons import dragon
            dragon()
            
        if player_stats['life'] <= 0:
            slow_print("You have lost all your lives and yet he still lives. You have failed to vanquish the ghost.")
            slow_print(f"                  Game OVER!\n{ascii.skull}")
            from main import beginning
            beginning()
            break
        elif ghost_stats['life'] <= 0:
            slow_print(f"You have vanquished the ghost. The dragon awaits.\n{ascii.map_cemetery_1}")
            from dragons import dragon
            dragon()
            return