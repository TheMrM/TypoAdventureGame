import ascii
from fight_forest import spider_fight_sword, spider_fight_bow
import characters
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Code that defines the forest goes here
def forest():
    slow_print(f"You have entered the forest. {ascii.map_forest}")
    slow_print("Entering the forest, the battle is nigh,")
    slow_print("A spider awaits, with sword and bow raised high.")
    slow_print(ascii.spider)
    
    # Code where players make decision to fight the spider with sword or bow
    weapon_choice = input("Which weapon do you choose? (sword/bow) ")
    if weapon_choice == "sword":
        slow_print(f"You have chosen the sword. {ascii.sword}")
        spider_fight_sword(characters.player_stats, characters.spider_stats)
    elif weapon_choice == "bow":
        slow_print(f"You have chosen the bow. {ascii.bow}")
        spider_fight_bow(characters.player_stats, characters.spider_stats)
    else:
        slow_print("Please choose a valid weapon.")
        forest()
