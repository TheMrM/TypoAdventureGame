import ascii
from fight_graveyard import ghost_fight_sword, ghost_fight_bow
import characters
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

#Code that defines the cemetary goes here
def cemetery():
    slow_print(f"You have entered the cemetery. {ascii.map_cemetery}")
    slow_print(f"Entering the cemetery, the battle is nigh,\nA ghost awaits, with sword and bow raised high.")
    slow_print(ascii.ghost)
    
#Code where player make decision to fight the ghost with sword or bow
    print("Which weapon do you choose? (sword/bow)")
    weapon_choice = input()
    if weapon_choice == "sword":
        slow_print(f"You have chosen the sword. {ascii.sword}")
        ghost_fight_sword(characters.player_stats, characters.ghost_stats)
    elif weapon_choice == "bow":
        slow_print(f"You have chosen the bow. {ascii.bow}")
        from fight_graveyard import ghost_fight_bow
        ghost_fight_bow(characters.player_stats, characters.ghost_stats)
    else:
        slow_print("Please choose a valid weapon.")
        cemetery()