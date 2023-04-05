
import ascii
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def beginning(delay_speed):
    while True:
        start_game = input("Do you want to start the game? (yes/no) ")
        if start_game.lower() == "yes":
            slow_print("Let's start the game!")
            def reset_player_stats():
                player_stats = {
                    'life': 5,
                }
            player_stats = reset_player_stats
            from path import path
            path()

        elif start_game.lower() == "no":
            slow_print(f"                  Game OVER!\n{ascii.skull}", delay_speed)
            break
        else:
            slow_print("Invalid choice. Please choose 'yes' or 'no'.", delay_speed)

if __name__ == "__main__":

    delay_speed = input("Welcome to the game! Please insert your desired speed :) \nYou may do so, by choosing a value between 1 and 5, from fastest(1) to slowest(5) :D We propose the value 3, if unsure. :)\n")
    while delay_speed not in "12345":
        delay_speed = input("Please insert a proper value :) ")
    delay_speed = int(delay_speed) * 0.01
    print(delay_speed)

    slow_print("In a far-off land, deep within a dense forest, there lived a mighty dragon.\nThe dragon was feared and respected by all who knew of it, for it was said\nthat the dragon possessed great power and wisdom. However, as mighty as\nthe dragon was, it was not invincible.", delay_speed)
    slow_print(f"Embark on the uncharted, where your map awaits, with adventure to create.\n{ascii.map}", delay_speed)
    beginning(delay_speed)