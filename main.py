from random import randint
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("too high")
        return turns -1
    elif user_guess < actual_answer:
        print("too low")
        return turns -1
    else:
        print(f"you get it! The answer is {actual_answer}")
#Function to set difficulty
def set_difficulty():
    level = input("choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    #choosing a random number between 1 and 100
    print("welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)


    #Let the user Guess a number
    turns = set_difficulty()
    print(f"you have {turns} attempts remaining to guess the number.")
    guess = 0
    while guess != answer:
        guess = int(input("make a guess: "))
        turns =  check_answer(guess, answer, turns)
        if turns == 0:
            # Track the number of turns and reduce by 1 if they get it wronge

            print("you've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")



    #Repeat the guessing functionality if they get it wrong
game()