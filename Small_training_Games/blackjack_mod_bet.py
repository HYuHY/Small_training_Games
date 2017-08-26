# Blackjack
# From 1 to 7 players compete against a dealer
# Players can make bets, if they haven't enough money
# they are sidelined.

import blackjack_mod

class BJ_Player_bet(blackjack_mod.BJ_Player):
	#money must be integer and above 0
	def __init__(self, name, money = 10):
		super(blackjack_mod.BJ_Player, self).__init__(name)
		self.money = money
		self.bet = 0
		
	def __str__(self):
		rep = super(blackjack_mod.BJ_Player, self).__str__()
		rep += "\t\tmoney: \t" + str(self.money)
		return rep

	def is_betting(self, bets_pool = (1,2,3,4,5)):
		# This is bet's value handler.
		bets_pool = [ bets_pool[i] for i in list(range(len(bets_pool))) if bets_pool[i] <= self.money]
		question = self.name + ", how much do you want bet? " + str(bets_pool) + "?\t\t"
		response = None
		while response not in bets_pool:
			try:
				response = int(input(question))
				if response > self.money :
					print("Too much. You haven't that money.")
					response = None
			except ValueError:
				print("Wrong bet. Enter another one")
		self.money -= response
		self.bet = response
		return response 
		
	
	def is_reward(self):
		self.money += self.bet*2
		self.bet = 0
	
	def is_losing(self):
		self.bet = 0
		
	def is_pushes(self):
		self.money += self.bet
		self.bet = 0

class BJ_Game_bet(blackjack_mod.BJ_Game):
	"""Allow to play with bets and remove players haven't enough money"""
	def __init__(self, names):	  
		self.players = []
		for name in names:
			player = BJ_Player_bet(name)
			self.players.append(player)

		self.dealer = blackjack_mod.BJ_Dealer("Dealer")
		self.deck = blackjack_mod.BJ_Deck()
		self.deck.populate()
		self.deck.shuffle()
	
	def sidelined(self):
		sp = []
		for player in self.players :
			if player.money > 0:
				sp.append(player)
		self.players = sp
		return self.players
		
	
	def play(self):
		if len(self.sidelined()) > 1 :
			
			# deal initial 2 cards to everyone
			self.deck.deal(self.players + [self.dealer], per_hand = 2)
			self.dealer.flip_first_card()	# hide dealer's first card
			for player in self.players:
				print(player)
				player.is_betting()
				print()
			print("\n")
			for player in self.players:
				print(player)
			print(self.dealer)

			# deal additional cards to players
			for player in self.players:
				self.additional_cards(player)

			self.dealer.flip_first_card()	# reveal dealer's first 

			if not self.still_playing:
				# since all players have busted, just show the dealer's hand
				print(self.dealer)
			else:
				# deal additional cards to dealer
				print(self.dealer)
				self.additional_cards(self.dealer)

				if self.dealer.is_busted():
					# everyone still playing wins
					for player in self.still_playing:
						player.win()
						player.is_reward()
				else:
					# compare each player still playing to dealer
					for player in self.still_playing:
						if player.total > self.dealer.total:
							player.win()
							player.is_reward()
						elif player.total < self.dealer.total:
							player.lose()
							player.is_losing()
						else:
							player.push()
							player.is_pushes()

			# remove everyone's cards
			for player in self.players:
				player.clear()
			self.dealer.clear()
		elif len(self.sidelined()) == 1 :
			print(self.players[0].name + " is win this circle of game! Congratulations!")
		else :
			print("All participant drop out.")


def main():
	import games
	
	print("\t\tWelcome to Blackjack with fancy bets!\n")
	print()
	
	names = ["Bo", "Kenzi", "Dayson", "Hale", "Trick"]
	
	circle = None
	while circle != "n":
		company = input("Use the default players or input new company? " \
		"Press Enter for the same or any key to start entering names: ")
		if company != '':
			number = games.ask_number("How many players? (1 - 7): ", low = 1, high = 8)
			names = []
			for i in range(number):
				name = input("Enter player name: ")
				names.append(name)
		
		game = BJ_Game_bet(names)
		number = len(names)
		
		again = None
		while again != "n":
			game.reinit(number)
			game.play()
			again = games.ask_yes_no("\nDo you want to play again?: ")
		
		circle = games.ask_yes_no("\nDo you want to start new circle of game?: ")


if __name__ == "__main__":
	main()
	input("\n\nPress the enter key to exit.")
