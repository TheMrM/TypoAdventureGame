import random
import ascii
from characters import *

def dragon_fight_sword(player_stats):
    from main import slow_print
    if player_stats['life'] <= 0:
        slow_print(f"You have {player_stats['life']} lives left.")
        slow_print(f"You have have layed your grave!")
        slow_print(f"Game OVER!\n{ascii.skull}")
        from main import beginning, delay_speed
        beginning(delay_speed)
    while True:
        slow_print("There is only two ways that the battle can end. You should 'roll' the dice to see if you will be the victor or the vanquished. ")
        roll = input()
        dice = random.randint(1, 6)
        if dice <= 5:
            slow_print("You have rolled a low dice. You have missed the dragon. The dragon has attacked you and you have lost 2 life.")
            player_stats['life'] -= 2
            slow_print(f"You have {player_stats['life']} lives left.")
            if player_stats['life'] <= 0:
                slow_print(f"Game OVER!\n{ascii.skull}")
                from main import beginning, delay_speed
                beginning(delay_speed)
                break
        else:
            slow_print("You have rolled high, the faith in your favor, but the dragon hide is stronger than ever")
            slow_print(f"Game OVER!\n{ascii.skull}")
            from main import beginning, delay_speed
            beginning(delay_speed)
            break

def dragon_fight_bow(player_stats, dragon_stats, delay_speed):
    if player_stats['life'] <= 0:
        print(f"You have {player_stats['life']} lives left.")
        print(f"You have have layed your grave!")
        print(f"Game OVER!\n{ascii.skull}")
        from main import beginning, delay_speed
        beginning(delay_speed)
    while True:
        print("There is only two ways that the battle can end, you should 'roll' the dice to see if you will be the victor or the vanquished. ")
        roll = input()
        dice = random.randint(1, 6)
        if dice <= 3:
            print("You have rolled a low dice. You have missed the dragon. The dragon has attacked you and you have lost 2 life.")
            player_stats['life'] -= 2
            print(f"You have {player_stats['life']} lives left.")
            if player_stats['life'] <= 0:
                from main import beginning, delay_speed
                beginning(delay_speed)
                print(f"                  Game OVER!\n{ascii.skull}")
                break
        elif dice <= 5:
            dragon_stats['life'] -= 5
            print("You have rolled high, the feith in your favor, and manage to mortaly woond the dragon.")
            print("Amidst the trials and challenges, I emerged victorious, strengthened by perseverance and determination.")
            print(f"                  Game OVER!\n{ascii.skull}")
            break