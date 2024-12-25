import random
def game(chances):
    target = random.randint(1,100)
    won=False
    for i in range(chances):
        try:
            curr_guess=int(input("\nEnter your guess: "))
            if(curr_guess==target):
                print(f"Congratulations! You guessed the correct number in {i+1} attempts.")
                won=True
                break;
            elif(curr_guess>target):
                print(f"Incorrect! The number is less than {curr_guess}.")
            else:
                print(f"Incorrect! The number is greater than {curr_guess}.")
        except:
            print("Please enter an integer between 1 and 100")
    if(won):
        print("\nHooray!! You won the game.")
    else:
        print("\nOops!! You exhausted your chances.")
        print(f"The number was {target}.")
    print("Thank You for playing.")


def intro():
    chances = {
        "Easy": 10,
        "Medium": 5,
        "Hard": 3
    }
    levels = ["Invalid", "Easy", "Medium", "Hard"]
    level = 0
    intro_text = """Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    You have 5 chances to guess the correct number.

    Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)"""

    print(intro_text)
    while (level == 0):
        try:
            curr_level = int(input("\nEnter your choice: "))
            if (curr_level >= 1 and curr_level <= 3):
                level = curr_level
            else:
                print("Invalid Choice")
        except:
            print("Please enter an integer")
    start_text = f"""\nGreat! You have selected the {levels[level]} difficulty level.\nLet's start the game!
            """
    print(start_text)
    game(chances[levels[level]])

if __name__=='__main__':
    intro()


