# Critter Caretaker
# A virtual pet to care for

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        print("Value 'hunger' :  ", self.hunger)
        print("Value 'boredom':  ", self.boredom)
        print("Property 'mood':  ", self.mood)
        return ''

    def __choose_option(self, options, options_pool):
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


def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Critter Caretaker
    
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
    
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()
        
        # feed your critter
        elif choice == "2":
            options = "How many pieces do you want to give? 1, 2, 3, 4 (Or 0):\n"
            options_pool = ('0','1','2','3','4')
            give = int(crit.__choose_option(options, options_pool))
            crit.eat(give)
         
        # play with your critter
        elif choice == "3":
            options = "How much time do you want to play with pet? 1, 2, 3, 4 minutes (Or 0):\n"
            options_pool = ('0','1','2','3','4')
            give = int(crit.__choose_option(options, options_pool))
            crit.play(give)

        # secret menu
        elif choice =='9':
            print(crit)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 
