# Card game 'War'
# From 1 to 7 players compete against each other. 
# They get only 1 card and player which value of card  better than others wins.

import games, blackjack_mod


class War_Game(blackjack_mod.BJ_Game):
	""" A War card game. """
	def __init__(self, names):	  
		self.players = []
		for name in names:
			player = blackjack_mod.BJ_Player(name)
			self.players.append(player)

		self.deck = blackjack_mod.BJ_Deck()
		self.deck.populate()
		self.deck.shuffle()

	def reinit(self, number):
		if (number)*5 > len(self.deck.cards) :
			self.deck = blackjack_mod.BJ_Deck()
			self.deck.populate()
			self.deck.shuffle()
			print("Deck is updated")

		   
	def play(self):
		# deal initial card to everyone
		self.deck.deal(self.players, per_hand = 1)
		for player in self.players:
			print(player)
		
		# sort result from max to min 
		end_scores = sorted(self.players, key = lambda x: x.total, reverse = True)
		print()
		for player in end_scores :
			# compare each player with winner
			if player.total == end_scores[0].total:
				player.win()
			
		# remove everyone's cards
		for player in self.players:
			player.clear()





def main():
	print("\t\tWelcome to War!\n")
	company = input("Use default players or input your company? " \
	"Press Enter for default or any key to start entering names: ")
	if company == '':
		names = ["Bo", "Kenzi", "Dayson", "Hale", "Trick"]
		number = len(names)
	else:
		number = games.ask_number("How many players? (1 - 7): ", low = 1, high = 8)
		for i in range(number):
			name = input("Enter player name: ")
			names.append(name)
	print()
	
	game = War_Game(names)

	again = None
	while again != "n":
		game.reinit(number)
		game.play()
		again = games.ask_yes_no("\nDo you want to play again?: ")
	
	
	
if __name__ == "__main__":
	main()
	input("\n\nPress the enter key to exit.")