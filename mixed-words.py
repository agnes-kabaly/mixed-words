################# Mixed words Game ##################
# The program displays a word with its letters mixed. 
# the user must guess the correct word.

import random

WORDLIST = ("codecool", "absztrahálás", "python", "ubuntu")

# Selects a word randomly from WORDLIST.
word = random.choice(WORDLIST)	
mixed_word = ''.join(random.sample(word,len(word)))
correct_answer = word

# start the game
print(
"""
           Welcome to the Mixed Words Game!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)

print("The mixed word is:", mixed_word)

user_input = input("Type your answer here: ")



