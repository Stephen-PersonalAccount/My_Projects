from Art import logo
from random import randint
print(logo)
print(" \nWelcome to the Number Guessing Game")
print("I'm thinking of a number betweeen 1 and 100")

player_difficulty_choice = input("Choose a difficulty level. Type 'easy' or 'hard': ").casefold()


def difficulty_based_on_difficulty_choice (player_difficulty_choice):
    """ Checks level of difficulty and returns the assigned number of attempts respectively"""
    valid_selection = False
    while not valid_selection:
        if player_difficulty_choice == "easy":
            attempts_allowed = 10
            valid_selection = True
        elif player_difficulty_choice == "hard":
            attempts_allowed = 5
            valid_selection = True
        else: 
            print("Please put a valid input")
            player_difficulty_choice = input("Choose a difficulty level. Type 'easy' or 'hard': ").casefold()

    return attempts_allowed



def actions ():
    """Checks player guess against the randomly generated number to decide a win or a loss"""
    random_generated_number = randint(1,100)
    num_of_attempts = difficulty_based_on_difficulty_choice(player_difficulty_choice)
    print(f"You have {num_of_attempts} attempts in total")
    game_on = True
    while game_on:
        
        if num_of_attempts == 0:
            print("Game Over, You Lost")
            game_on = False
        else:
            player_guess = int(input("Make a guess: "))
            if player_guess > random_generated_number:
                num_of_attempts -= 1
                print(f"Too high \nYou have {num_of_attempts} attempts remaining to guess the number.")
            elif player_guess < random_generated_number:
                num_of_attempts -= 1
                print(f"Too low \nYou have {num_of_attempts} attempts remaining to guess the number.")
            elif player_guess == random_generated_number:
                print(f"Correct \nThe hidden number is {random_generated_number}.")
                game_on = False
            


actions()
