# coding: utf-8

# Computer Guess My Number
"""
 The user inputs a random number between 1 and 100
 The computer tries to guess it and lets
 the player know what number was tried
"""
import random

print("Welcome to 'Comp Guess My Number'!")

the_number = 1000
while the_number > 100 or the_number < 1 :
	print("Please enter a number between 1 and 100\n")
	the_number = int(input())

print("you choose the_number =", the_number)
try_count = 0
try_flag = 1
right_point = 1
left_point = 100
guess = right_point + (left_point - right_point)//2

while try_flag :
	try_count += 1
	print(guess)
	if guess == the_number:
		try_flag = 0
		print("Your number is", guess,"\nAttempts:",try_count)
	elif guess < the_number :
		right_point = guess
		delta = (left_point - right_point)//2
		if delta == 0:
			delta = 1
		guess = right_point + delta
	elif guess > the_number :
		left_point = guess
		delta = (left_point - right_point)//2
		if delta == 0:
			delta = 1
		guess = left_point - delta

input("Push Enter to close program")
