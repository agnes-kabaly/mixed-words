################# Mixed words Game ##################
# The program displays a word with its letters mixed.
# the user must guess the correct word.
#  (sys.exit()
import sys
import random

# Selects a word randomly from imported_wordlist.txt.
# imported_wordlist.txt
# imp_codecool.txt
# imp_python.txt
def import_wordlist(filename):
    word = (random.choice(open(filename, 'r').read().splitlines()))
    mixed_word = ''.join(random.sample(word,len(word)))
    correct_answer = word
    return mixed_word, correct_answer

def player_ask():
    while True:
        mixed_word = ""
        correct_answer = ""
        filename = ""
        print("   Now you can choose 'Your' category! :)\n")
        ask_input = input("\t'R' for Random Words\n\t'C' for Codecool\n\t'P' for PYTHON\n")
        if ask_input == "r" or ask_input == "R":
            mixed_word, correct_answer = import_wordlist("imported_wordlist.txt")
            print("\n   You choose: Random Words List\n")
            break
        elif ask_input == "c" or ask_input == "C":
            mixed_word, correct_answer = import_wordlist("imp_codecool.txt")
            print("\n   You choose: Codecool Word List\n")
            break
        elif ask_input == "p" or ask_input == "P":
            mixed_word, correct_answer = import_wordlist("imp_python.txt")
            print("\n   You choose: PYTHON Words List\n")
            break
        elif ask_input == "q":
            print("\nSorry to see you go.")
            sys.exit()
        elif ask_input != "":
            print("Invalid input, please type in the correct form!\n:)")
        else:
            print("Invalid input, please type in the correct form!\n:)")
    return mixed_word, correct_answer

life = 3

# start the game
print(
"""
           Welcome to the Mixed Words Game!

   Unscramble the letters to make a word.
(Press the q key to quit.)
"""
)

mixed_word, correct_answer = player_ask()

print("Max lives:", life, "\n")

running = 1
while running == 1:
    print("The mixed word is:", mixed_word)
    user_input = input("Type your answer here: ")
    if user_input != correct_answer:
        print("Your answer was incorrect. Try again!\n")
        life -= 1
        print("You have", life, "lives left.\n")
        if life == 0:
            print(
            r"""
             _____       ___       ___  ___   _____
            /  ___|     /   |     /   |/   | |  ___|
            | |        / /| |    / /|   /| | | |__
            | |  _    / ___ |   / / |__/ | | |  __|
            | |_| |  / /  | |  / /       | | | |___
            \_____/ /_/   |_| /_/        |_| |_____|
             _____   _     _   _____   _____
            /  _  \ | |   / / |  ___| |  _  \
            | | | | | |  / /  | |__   | |_| |
            | | | | | | / /   |  __|  |  _  /
            | |_| | | |/ /    | |___  | | \ \
            \_____/ |___/     |_____| |_|  \_\
            """
            )
            quit()
    elif user_input == "q":
        life += life + 1
        print("Sorry to see you go.")
        sys.exit()
    elif user_input == correct_answer:
        print("Success!!! Your answer:", correct_answer, "was correct.\n")
        word = (random.choice(open("imported_wordlist.txt", 'r').read().splitlines()))
        mixed_word = ''.join(random.sample(word,len(word)))
#        print("Success!!! Your answer:", correct_answer, "was correct.\n")
        correct_answer = word
#        del correct_answer
#        word = (random.choice(open(filename, 'r').read().splitlines()))
#        mixed_word = ''.join(random.sample(word,len(word)))
    if user_input == "q":
        life += life + 1
        print("Sorry to see you go.")
        break
