# TV imitation
# TV as a programming object-oriented type

class TV(object):
	"""An imitation of TV"""
	
	def __init__(self, model, min_channel = 0, max_channel = 99, 
				min_volume = 0, max_volume = 100):
		self.__model = model
		self.__channel = min_channel
		self.__min_channel = min_channel
		self.__max_channel = max_channel
		self.__min_volume = min_volume
		self.__max_volume = max_volume
		self.__volume = (max_volume + min_volume) // 2
	
	def __str__(self):
		#Show feature of TV model
		m = self.__max_channel - self.__min_channel + 1
		print("That imitation of TV, model name:  ", self.__model)
		print("Default settings: number of channels ", m, 
			"volume range from ", self.__min_volume, "to ", self.__max_volume)
		return ''
		
	def __choose_option(self, options, options_pool):
		#Check correctness of choosed options
		print(options)
		choice = input()
		wrong = True
		
		while wrong :
			if choice == "":
				wrong = False
			else: 
				try:
					choice = int(choice)
					if options_pool[0] > choice or options_pool[1] < choice:
						print("Wrong value. Only from ", options_pool[0], 
								" to ", options_pool[1], "Try again: ")
						choice = input()
					else :
						wrong = False
				except ValueError as e:
					print("Wrong value. Only from ", options_pool[0], 
								" to ", options_pool[1], "Try again: ")
					choice = input()
		
		print()
		return choice
	
	@property
	def characteristics(self):
		print(" Model name:    ", self.__model, "\n",
		"Channels range: from ", self.__min_channel, " to ", 
		self.__max_channel, "\n"
		" Volume range:   from ", self.__min_volume, " to ", 
		self.__max_volume)


	def set_volume(self):
		OPTIONS_1 = ('''
		Input value of volume you want to set (from 0 to 100)
		or press Enter to retain current significance: ''')
		OPTIONS_POOL_1 = (self.__min_volume, self.__max_volume)
		choice = self.__choose_option(OPTIONS_1, OPTIONS_POOL_1)
		if choice != "" :
			self.__volume = choice
		print("Volume was set to: ", self.__volume)
	
	def set_channel(self):
		OPTIONS_2 = ('''
		Input channel number you want to watch 
		or press Enter to retain current significance: ''')
		OPTIONS_POOL_2 = (self.__min_channel, self.__max_channel)
		choice = self.__choose_option(OPTIONS_2, OPTIONS_POOL_2)
		if choice != "" :
			self.__channel = choice
		print("Now you switch to channel: ", self.__channel)
	
	

def main():
	tv_1 = input("Enter model name of your TV: ")
	
	if tv_1 == '':
		tv_1 = TV('default')
	else :
		tv_1 = TV(tv_1)
	
	
	select = None
	while select != "0":
		print('''
		TV imitation
		0 - Shut down TV imitation
		1 - Choose channel
		2 - Set volume
		''')
		select = input("Your choice: ")
		print()
		
		# Exit
		if select == '0':
			print("Arrrrghh!..")
		
		# Choose channel
		elif select == '1':
			tv_1.set_channel()
		
		# Choose volume
		elif select == '2':
			tv_1.set_volume()
		
		# Hidden option 1
		elif select == '3':
			tv_1.characteristics
		
		# Hidden option 2
		elif select == '4':
			print(tv_1)
		
		# Some unknown choice
		else :
			print("\nSorry, but", select, "isn't a valid choice.")
	
main()
input("Press Enter to escape")