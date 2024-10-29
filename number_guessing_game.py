import random
import time

# Function to get a valid number from the user
def get_valid_number(prompt, start, end):
    while True:
        try:
            guess = int(input(prompt))
            if start <= guess <= end:
                return guess
            else:
                print(f"Please enter a number between {start} and {end}.")
        except ValueError:
            print("Oops! That's not a valid number. Try again.")

# Difficulty selection
def choose_difficulty():
    print("Choose your difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-100)")
    print("3. Hard (1-1000)")
    print("4. Hard (1-2000)")
    level = get_valid_number("Enter 1, 2, or 3: ", 1, 3)
    if level == 1:
        return 1, 10
    elif level == 2:
        return 1, 100
    else:
        return 1, 1000

def play_game():
    print("Welcome to the Number Guessing Game!")
    start, end = choose_difficulty()
    secret_number = random.randint(start, end)
    print(f"I've picked a number between {start} and {end}. Can you guess what it is?")
    
    user_guess = None
    attempts = 0
    start_time = time.time()
    
    while user_guess != secret_number:
        user_guess = get_valid_number(f"Enter your guess between {start} and {end}: ", start, end)
        attempts += 1
        
        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        
        if attempts == 5:
            if secret_number % 2 == 0:
                print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")
    
    print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
    end_time = time.time()
    print(f"It took you {round(end_time - start_time, 2)} seconds to guess the number.")
    
    if play_again():
        print("\nRestarting the game...\n")
        play_game()
    else:
        print("Thanks for playing! See you next time!")

def play_again():
    response = input("Do you want to play again? (yes/no): ").lower()
    return response == 'yes'

play_game()
