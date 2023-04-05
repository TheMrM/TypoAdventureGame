import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
def path():
    while True:
        path_choice = input("Which path do you choose? (left/right) ")
        if path_choice == "left":
            slow_print("You have chosen the left path. Adventure awaits!")
            from trees import forest
            forest()
            return path_choice
        
        if path_choice == "right":
            slow_print("You have chosen the right path. Adventure awaits!")
            from graveyard import cemetery
            cemetery()
            return path_choice
        else:
            slow_print("Invalid choice. Please choose 'left' or 'right'.")
            return path_choice