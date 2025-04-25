import random

flag = True

while flag:
    print("New game started.\n")
    random_number = random.randint(1, 100)
    player_life = 5

    while True:
        print(f"Your remaining attempts: {player_life}")
        try:
            number = int(input("Guess a number between 1 and 100: "))
            if number < 1 or number > 100:
                print("Please enter a number between 1 and 100!")
                continue
        except ValueError:
            print("Please enter a valid number!")
            continue
        if number == random_number:
            print(f"Correct! You guessed the number {random_number}. You win!")
            break
        elif number < random_number:
            print("Too low! Try a higher number.")
            player_life -= 1  
        else:
            print("Too high! Try a lower number.")
            player_life -= 1
        
        if player_life == 0:
            print(f"Game over! The number was {random_number}")
            break
    while True:
        new_game = input("Do you want to play again? (yes/no): ").lower()
        if new_game in ["yes", "no"]:
            break
        print("Please enter 'yes' or 'no'!")
    flag = new_game == "yes"
    