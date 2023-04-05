import ascii
import characters
from characters import player_stats
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def dragon_fight():
    slow_print("With no time to waist, you must choose wisely? (sword/bow) ")
    weapon_choice = input()
    if weapon_choice == "sword":
        slow_print(ascii.sword)
        from fight_dragon import dragon_fight_sword
        dragon_fight_sword(characters.player_stats)
        if player_stats['life'] <= 0:
            slow_print(f"                  Game OVER!\n{ascii.skull}")
            return False
    elif weapon_choice == "bow":
        slow_print(ascii.bow)
        from fight_dragon import dragon_fight_bow
        dragon_fight_bow(characters.player_stats, characters.dragon_stats)
        if player_stats['life'] <= 0:
            slow_print(f"                  Game OVER!\n{ascii.skull}")
            return False
    else:
        slow_print("Invalid choice. Please choose either 'sword' or 'bow'.")
        return False

    return True

def dragon():
    slow_print(f"Your journey has come to an end. The dragon awaits. {ascii.map_finish}")
    slow_print(f"You have entered the castle with no one in sight. {ascii.castle}")
    slow_print(f"Is that a thunrering sound? {ascii.fire}")
    slow_print("Dragon's flaps so strong and grand, they shake the earth and move the land.")
    slow_print(f"Is that a dragon? {ascii.dragon}")
    slow_print("You have entered my eralm, here I am king, just draw your weapon and prepare to be my meal.")
    
    while True:
        if not dragon_fight():
            slow_print("Do you want to start the game? (yes/no) ")
            play_again = input()
            if play_again == "yes":
                characters.player_stats = 5
                continue
            else:
                break
        else:
            break
