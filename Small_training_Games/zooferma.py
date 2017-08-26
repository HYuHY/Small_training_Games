# Zoofarm base on Critter Caretaker
# Virtual pets to care for


class Critter(object):
	"""A virtual pet"""
	def __init__(self, name):
		import random
		self.name = name
		self.hunger = random.randint(0, 8)
		self.boredom = random.randint(0, 8)

	def __str__(self):
		print("Value 'hunger' :  ", self.hunger)
		print("Value 'boredom':  ", self.boredom)
		print("Property 'mood':  ", self.mood)
		return ''

	def choose_option(self, options, options_pool):
		#Check correctness of choosed options
		print(options)
		choice = input ("Your choice: ")
		while choice not in options_pool :
			if choice != None :
				print("This option does not exist\n")
				choice = input ("Your choice: ")
		print()
		return choice
        
        
	def __pass_time(self):
		self.hunger += 1
		self.boredom += 1

	@property
	def mood(self):
		unhappiness = self.hunger + self.boredom
		if unhappiness < 5:
			m = "happy"
		elif 5 <= unhappiness <= 10:
			m = "okay"
		elif 11 <= unhappiness <= 15:
			m = "frustrated"
		else:
			m = "mad"
		return m
    
	def talk(self):
		print("I'm", self.name, "and I feel", self.mood, "now.\n")
		self.__pass_time()
    
	def eat(self, food = 4):
		print("Brruppp.  Thank you.")
		self.hunger -= food
		if self.hunger < 0:
			self.hunger = 0
		self.__pass_time()

	def play(self, fun = 4):
		print("Wheee!")
		self.boredom -= fun
		if self.boredom < 0:
			self.boredom = 0
		self.__pass_time()
		


		
		
		
def main(max_pets = 9, default = 3):
	
	# Choose number of pet on zoo farm
	wrong = True
	number = None
	print(" How many pet on your farm? Enter the number\n", 
	"(but no more ", max_pets, " and above 0).\n", 
	"Please note, that then you must give every of them a name.\n",
	"Or input '0' to exit. Or press Enter for default setting. Number: ")
	while wrong:
		number = input()
		try:
			if number != '':
				number = int(number)
			if number == '':
				print("You choose default number of pets: 3")
				number = default
				wrong = False
			elif (int(number) > max_pets and int(number) < 0):
				print("Wrong value. Only above 0 to ", max_pets , ". Try again (Or 0 to exit): ")
			elif int(number) == 0 :
				wrong = False
				return "Oh, all pets are dead long ago! Press Enter to burn them"
			else :
				wrong = False
		except ValueError :
			print("Wrong value. Only from 0 to ", max_pets , ". Try again (Or 0 to exit): ")
	
	#Creation of zoofarm
	zoofarm = []
	for i in range (0, number):
		name = input("Enter a name of "+str(i+1)+" pet:")
		zoofarm.append(Critter(name))

	choice = None  
	while choice != "0":
		print \
		("""
		Critters Zoofarm Caretaker
	
		0 - Quit
		1 - Listen to your critters
		2 - Feed your critters
		3 - Play with your critters
		""")
	
		choice = input("Choice: ")
		print()
		
		# exit
		if choice == "0":
			print("Good-bye.")

		# listen to your critters
		elif choice == "1":
			for i in range (0, number):
				zoofarm[i].talk()
        
		# feed your critters
		elif choice == "2":
			options = "How many pieces do you want to give? 1, 2, 3, 4 (Or 0):\n"
			options_pool = ('0','1','2','3','4')
			give = int(zoofarm[0].choose_option(options, options_pool))
			for i in range (0, number):
				zoofarm[i].eat(give)
         
		# play with your critters
		elif choice == "3":
			options = "How much time do you want to play with pet? 1, 2, 3, 4 minutes (Or 0):\n"
			options_pool = ('0','1','2','3','4')
			give = int(zoofarm[0].choose_option(options, options_pool))
			for i in range (0, number):
				zoofarm[i].play(give)

		# secret menu
		elif choice =='9':
			for i in range (0, number):
				print(zoofarm[i])

		# some unknown choice
		else:
			print("\nSorry, but", choice, "isn't a valid choice.")
	
	return "Press Enter to escape"


answer = main()
input(answer)