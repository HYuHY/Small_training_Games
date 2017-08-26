def ask_number(question, low, high, interval = 1):
	"""Ask for a number within a range."""
	response = None
	print("Possible answers: from ", low, " to ", high, " with interval ",interval)
	while response not in range(low, high, interval):
		response = int(input(question))
	return response


test = ask_number("How many girls would you fuck? (from 1 to 8) ", 1, 8, interval = 3 )
print("so be it, ", test, " girl")
input("Press Enter to escape")