# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

def ask_number(question, low, high, interval = 1):
	"""Ask for a number within a range."""
	response = None
	print("Possible answers: from ", low, " to ", high, " with interval ",interval)
	while response not in range(low, high, interval):
		response = int(input(question))
	return response

def main():
	print("\tWelcome to 'Guess My Number'!")
	print("\nI'm thinking of a number between 1 and 100.")
	print("Try to guess it in as few attempts as possible.\n")

	# set the initial values
	limit_try = random.randint(3, 4)
	print("You have", limit_try, "tries\n")

	the_number = random.randint(1, 100)
	guess = int(input("Take a guess: "))
	tries = 1

	# guessing loop
	while guess != the_number and tries < limit_try:
		if guess > the_number:
			print("Lower...")
		else:
			print("Higher...")

		guess = ask_number("Take a guess: ", 1, 100, interval = 1 )
		tries += 1
	if guess != the_number and tries == limit_try:
		print("Как можно было это не угадать? у тебя что,"\
		+"удача вообще на 0? \nВы там живы ещё, с таким везением, а?")
		print("The number was", the_number)
	elif guess == the_number:
		print("You guessed it!  The number was", the_number)
		print("And it only took you", tries, "tries!\n")
  
	input("\n\nPress the enter key to exit.")
	
main()
