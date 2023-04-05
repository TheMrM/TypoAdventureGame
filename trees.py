import ascii
from fight_forest import spider_fight_sword, spider_fight_bow
import characters
from main import slow_print

# Code that defines the forest goes here
def forest(delay_speed):
    slow_print(f"You have entered the forest. {ascii.map_forest}", delay_speed)
    slow_print("Entering the forest, the battle is nigh,", delay_speed)
    slow_print("A spider awaits, with sword and bow raised high.", delay_speed)
    slow_print(ascii.spider)
    
    # Code where players make decision to fight the spider with sword or bow
    weapon_choice = input("Which weapon do you choose? (sword/bow) ")
    if weapon_choice == "sword":
        slow_print(f"You have chosen the sword. {ascii.sword}", delay_speed)
        spider_fight_sword(characters.player_stats, characters.spider_stats, delay_speed)
    elif weapon_choice == "bow":
        slow_print(f"You have chosen the bow. {ascii.bow}", delay_speed)
        spider_fight_bow(characters.player_stats, characters.spider_stats, delay_speed)
    else:
        slow_print("Please choose a valid weapon.", delay_speed)
        forest(delay_speed)
