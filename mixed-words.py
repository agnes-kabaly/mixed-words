################# Mixed words Game ##################
# The program displays a word with its letters mixed.
# the user must guess the correct word.

import random

WORDLIST = ("codecool", "absztrahálás", "python", "ubuntu", "csibefasirt", "imibot", "pycon")

# Selects a word randomly from WORDLIST.
word = random.choice(WORDLIST)
mixed_word = ''.join(random.sample(word,len(word)))
correct_answer = word

life = 3

# start the game
print(
"""
           Welcome to the Mixed Words Game!

   Unscramble the letters to make a word.
(Press the q key to quit.)
"""
)

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
        elif user_input == correct_answer:
                word = random.choice(WORDLIST)
                mixed_word = ''.join(random.sample(word,len(word)))
                print("Success!!! Your answer:", correct_answer, "was correct.\n")
                correct_answer = word
        if user_input == "q":
           print("Sorry to see you go.")
           break
