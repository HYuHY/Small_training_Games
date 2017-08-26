# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word
# create a prompt to use later to see if the some guesses is wrong
PROMPT_word = correct[ :(len(correct))//3]


# create a jumbled version of the word
jumble =""
while word:
	position = random.randrange(len(word))
	jumble += word[position]
	word = word[:position] + word[(position + 1):]

PROMPTS = tuple( WORDS[i][ :(len(WORDS[i]))//3] for i in range(len(WORDS)))

	
# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

fail_count = 0
guess = input("\nYour guess: ")
while guess != correct and guess != "":
	print("Sorry, that's not it.")
	fail_count += 1
	if fail_count == len(PROMPT_word) :
		print("You gave ", fail_count," wrong answers. So you get a prompt.",
			 " First letters of word is: ", PROMPT_word)
	guess = input("Your guess: ")
	
#Начисление баллов зависит от длины слова и количества ошибок
mark = len(correct) - fail_count
    
if guess == correct:
	print("That's it!  You guessed it!\n", 
		"You gave ", fail_count, " wrong aswers in total\n",
		"So You score is ", mark)

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")