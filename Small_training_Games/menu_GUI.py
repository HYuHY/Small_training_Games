# Menu GUI
# Create menu , with opportunity to point which meal you prefer
# and to calculate summary payment for it

from tkinter import *
import sys

class Application(Frame):
	""" GUI application that makes menu from file."""
	def __init__(self, master, table):
		""" Initialize Frame. """
		# set the initial values
		import sys
		self.table = table
		super(Application, self).__init__(master)  
		self.grid()
		self.create_widgets()
		
	def create_widgets(self):
		""" Create widgets to get menu item and to display name, weight, price"""
		# create instruction and legend labels
		Label(self,
			  text = "Welcome to our restaurant! Today we may offer you next dishes"
			  ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
		Label(self,
			  text = "Kind of Dish"
			  ).grid(row = 1, column = 0, columnspan = 1, sticky = W)
		Label(self,
			  text = "Weight of portion, g"
			  ).grid(row = 1, column = 1, columnspan = 1, sticky = W)
		Label(self,
			  text = "Energy value, kkal"
			  ).grid(row = 1, column = 2, columnspan = 1, sticky = W)
		Label(self,
			  text = "Cost, rub"
			  ).grid(row = 1, column = 4, columnspan = 1, sticky = W)
		Label(self,
			  text = "Order , y/n"
			  ).grid(row = 1, column = 5, columnspan = 1, sticky = W)
		Label(self,
			  text = "Quantity , pcs"
			  ).grid(row = 1, column = 6, columnspan = 1, sticky = W)
		

		# create check buttons and label with description for meal
		for i in range(len(self.table)):
			self.table[i][5] = IntVar()  # перем. для галки заказать/не заказать
			Checkbutton(self,   
						text = "",
						variable = self.table[i][5],
						onvalue = 1, offvalue = 0
						).grid(row = i*3+2, column = 5, sticky = W)
			# create label with description for meal
			Label(self,
				  text = self.table[i][0]
				  ).grid(row = i*3+2, column = 0, columnspan = 1, sticky = W)
			Label(self,
				  text = self.table[i][1]
				  ).grid(row = i*3+2, column = 1, columnspan = 1, sticky = W)
			Label(self,
				  text = self.table[i][3]
				  ).grid(row = i*3+2, column = 2, columnspan = 1, sticky = W)
			Label(self,
				  text = self.table[i][4]
				  ).grid(row = i*3+2, column = 4, columnspan = 1, sticky = W)
			Label(self,
				  text = self.table[i][2]
				  ).grid(row = i*3+3, column = 0, columnspan = 2, sticky = W)
			Label(self,
				  text = ""
				  ).grid(row = i*3+4, column = 0, columnspan = 2, sticky = W)
			# create entry for meal quantity 
			self.table[i][6] = Entry(self)
			self.table[i][6].grid(row = i*3+2, column = 6, sticky = W)
		
		# create label with summary value of order
		Label(self,
			  text = "Summary value of order: "
			  ).grid(row = len(self.table)*3+4, column = 0, columnspan = 1, sticky = W)

		# making python/tkinter label widget update with summary value of order
		self.response = StringVar()
		Label(self,
		      textvariable = self.response
		      ).grid(row = len(self.table)*3+4, column = 4, columnspan = 1, sticky = W)
		self.response.set("0") 
		
		# create a submit button
		Button(self,
			   text = "Calculate",
			   command = self.calc_order
			   ).grid(row = len(self.table)*3+4, column = 2, columnspan = 2, sticky = W)

		self.status_txt = Text(self, width = 125, height = 10, wrap = WORD)
		self.status_txt.grid(row = len(self.table)*3+5, column = 0, columnspan = 7)
		
	def calc_order(self):
		# get values from the GUI
		sum = 0
		for i in range(len(self.table)):
			meal_quant = self.table[i][6].get()
			try:
				if meal_quant != "" :
					meal_quant = int(meal_quant)
				else:
					meal_quant = 1
			except ValueError :
				meal_quant = 0
			meal = self.table[i][5].get()
			sum += float(self.table[i][4]) * meal * meal_quant
		self.response.set(str(sum))

# read menu's records from txt file with 5 line on one record-list
def read_record(restaraunt_menu = 'restaraunt_menu.txt'):
	table = []
	try:
		record_file = open(restaraunt_menu, 'r')
		table_raw = record_file.readlines()
		for i in range(0, len(table_raw)//5) :
			table.append([])
			for j in range(5):
				table[i].append(table_raw[5*i+j].strip('\n'))
			table[i].append(0)
			table[i].append(0)
		record_file.close()
	except (EOFError, FileNotFoundError):
		pass
	return table
		
		
# main
table = read_record()
root = Tk()
root.title("Menu GUI")
app = Application(root, table)
root.mainloop()
