import random
# import ascii
from characters import *
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
def dragon_fight_sword(player_stats):
    while True:
        slow_print("There is only two ways that the battle can end. You should 'roll' the dice to see if you will be the victor or the vanquished. ")
        roll = input()
        dice = random.randint(1, 6)
        if dice <= 5:
            slow_print("You have rolled a low dice. You have missed the dragon. The dragon has attacked you and you have lost 2 life.")
            player_stats['life'] -= 2
            slow_print(f"You have {player_stats['life']} lives left.")
            if player_stats['life'] <= 0:
                from main import beginning
                beginning()
                print(f"                  Game OVER!\n{ascii.skull}")
                break
        else:
            slow_print("You have rolled high, the faith in your favor, but the dragon hide is stronger than ever")
            # print(f"                  Game OVER!\n{ascii.skull}")
            break

def dragon_fight_bow(player_stats, dragon_stats):
    while True:
        slow_print("There is only two ways that the battle can end, you should 'roll' the dice to see if you will be the victor or the vanquished. ")
        roll = input()
        dice = random.randint(1, 6)
        if dice <= 3:
            slow_print("You have rolled a low dice. You have missed the dragon. The dragon has attacked you and you have lost 2 life.")
            player_stats['life'] -= 2
            slow_print(f"You have {player_stats['life']} lives left.")
            if player_stats['life'] <= 0:
                from main import beginning
                beginning()
                # print(f"                  Game OVER!\n{ascii.skull}")
                break
        elif dice <= 5:
            dragon_stats['life'] -= 5
            slow_print("You have rolled high, the feith in your favor, and manage to mortaly woond the dragon.")
            slow_print("Amidst the trials and challenges, I emerged victorious, strengthened by perseverance and determination.")
            # print(f"                  Game OVER!\n{ascii.skull}")
            break