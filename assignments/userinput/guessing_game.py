from pickle import NONE


def start():
    '''
    This function starts the guessing game loop logic. The function will poll and wait
    until the user inputs their guess and will exit once some conditions are met.
    '''
    # User must guess the correct animal that I have chosen

    total_guesses = 3
    attempt = 0

    answer = "dog" 
    guess = None
    while guess != answer:
        guess = input("Guess animal: ").lower()
        attempt += 1
        if guess == answer:
            print("Congrats you won, Go Home")
            break
        elif attempt == total_guesses:
            print("Out of guesses!")
            break
        elif attempt == total_guesses:
            quit
            break
        else:
            print("Wrong answer, Guess again")

    return answer # replace this line with your game loop logic.

    
start()