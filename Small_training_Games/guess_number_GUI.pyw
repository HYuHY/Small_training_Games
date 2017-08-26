# Crazy Tales
# Create a story based on user input

from tkinter import *

class Application(Frame):
	""" GUI application that makes little game with user guessing number. """


	
	def __init__(self, master):
		""" Initialize Frame. """
		# set the initial values
		import random
		self.limit_try = random.randint(5, 9)
		self.the_number = str(random.randint(1, 100))
		self.tries = 0
		self.win = 0
		self.options_pool = [str(list(range(1,101))[i]) for i in list(range(100))]
		
		super(Application, self).__init__(master)  
		self.grid()
		self.create_widgets()
		

	
	def create_widgets(self):
		""" Create widgets to get number and to display prompts. """
		
		# create instruction label
		Label(self,
		      text = "Welcome to 'Guess My Number'!"
		      ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
		Label(self,
		      text = "I'm thinking of a number between 1 and 100."
		      ).grid(row = 1, column = 0, columnspan = 2, sticky = W)
		Label(self,
		      text = "Try to guess it in as few attempts as possible."
		      ).grid(row = 2, column = 0, columnspan = 2, sticky = W)
		
		# making python/tkinter label widget update with attempts left
		self.attempts = StringVar()
		Label(self,
		      textvariable = self.attempts,
		      ).grid(row = 3, column = 0, columnspan = 2, sticky = W)
		self.attempts.set("You have " + str(self.limit_try - self.tries) + " attempts")  

		# create a label and text entry for a player's guess
		Label(self,
			  text = "Take a guess: "
			  ).grid(row = 4, column = 0, sticky = W)
		self.guess_ent = Entry(self)
		self.guess_ent.grid(row = 4, column = 1, sticky = W)
		
		# making python/tkinter label widget update with status input check
		self.response = StringVar()
		Label(self,
		      textvariable = self.response,
		      ).grid(row = 5, column = 0, columnspan = 2, sticky = W)
		self.response.set("Input integer number between 1 and 100") 
	
		# create a submit button
		Button(self,
			   text = "Check the guess",
			   command = self.check_guess
			   ).grid(row = 4, column = 2, sticky = W)

		self.status_txt = Text(self, width = 125, height = 10, wrap = WORD)
		self.status_txt.grid(row = 6, column = 0, columnspan = 4)
		

	
	
	def check_guess(self):
		""" Fill status text box with responce based on user guess. """
		# get values from the GUI
		guess = self.guess_ent.get()
		if guess not in self.options_pool :
			self.response.set("Wrong value. It must be integer number" +
			" from 1 to 100. Try again")
		else :
			if self.win == 0:
				self.tries += 1
				self.response.set("")
				if guess != self.the_number and self.tries <= self.limit_try:
					self.status_txt.insert(0.0, guess)
					self.attempts.set("You have " + str(self.limit_try - self.tries) + " attempts")
					if guess > self.the_number:
						self.status_txt.insert(0.0, "\nLower...")
					else:
						self.status_txt.insert(0.0, "\nHigher...")
				elif self.tries > self.limit_try:
					self.win = 1
					self.response.set("You have used all attempts or guessed the number, restart game's window" )
					self.status_txt.insert(0.0, "\nWell, you'll be lucky next time.")
					self.status_txt.insert(0.0, "\nThe number was " + self.the_number)
					self.status_txt.insert(0.0, "\nRestart game's window for another game.")
				elif guess == self.the_number and self.tries <= self.limit_try :
					self.status_txt.insert(0.0, "\nYou guessed it!  The number was " + self.the_number)
					self.status_txt.insert(0.0, "\nRestart game's window for another game.")
					self.win = 1


if __name__ == "__main__":
	root = Tk()
	root.title("Guess Number GUI")
	app = Application(root)
	root.mainloop()