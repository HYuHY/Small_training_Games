# Угадай слово
#
# Компьютер выбирает некое слово (существительное)из внесённого в 
# программу списка.
# Игроку сообщается, сколько букв в слове и даётся несколько попыток 
# узнать, есть ли какая-либо предложенная игроком буква в слове. 
# Программа отвечает только "да" или "нет". После чего игрок должен
# попробовать отгадать слово с определённого числа попыток, зависящего
# от количества оставшихся неопознанных букв.
# 

import random

WORDS = ("теория", "интерес", "заговор", "сотворение", "реальность", 
		"высказывание", "зрение", "альтернатива")
word = random.choice(WORDS)
correct = word
letters_count = len(correct)//2 +2

print("В загаданном слове ", len(correct), " букв\n",
	"Осталось попыток угадывания букв: ", letters_count)

guess = None
while letters_count > 0 and guess != "" :
	guess = input("\nCharacter, Your guess (will be consider \
					only one first symbol ): ")
	letters_count -= 1
	if guess in correct :
		print("\nThat is right, there is character \"", guess, "\" in word")
	else :
		print("\nNo, this symbol is absent")

print("\nNow try to guess the whole word. You have 2 attempts")
guess = input("\nYour guess: ")
fail_count = 0
while guess != correct and guess != "" and fail_count != 2 :
	print("Sorry, that's not it.")
	fail_count += 1
	guess = input("\nYour next guess: ")
		
if guess == correct:
	print("That's it!  You guessed it!\n", 
		"The word is really was   \" ", correct,"\"")

input("\n\nPress the enter key to exit.")
