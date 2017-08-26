# Crazy Tales
# Create a story based on user input

from tkinter import *


class Application(Frame):
	""" GUI application that creates a story based on user input. """
	def __init__(self, master):
		""" Initialize Frame. """
		super(Application, self).__init__(master)  
		self.grid()
		self.create_widgets()
		
	def create_widgets(self):
		""" Create widgets to get story information and to display story. """
		# create instruction label
		Label(self,
		      text = "Введите новые постулаты для бредогенерации"
		      ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

		# create a label and text entry for the name of a person
		Label(self,
			  text = "Личность (муж.род): "
			  ).grid(row = 1, column = 0, sticky = W)
		self.person_ent = Entry(self)
		self.person_ent.grid(row = 1, column = 1, sticky = W)
		
		# create a label and text entry for a verb
		Label(self,
			  text = "Глагол (инфинитив): "
			  ).grid(row = 2, column = 0, sticky = W)
		self.verb_ent = Entry(self)
		self.verb_ent.grid(row = 2, column = 1, sticky = W)
		
		# create a label for verbs check buttons
		Label(self,
			  text = "Глаголы (предызбранные):"
			  ).grid(row = 3, column = 0, sticky = W)

		# create verb_1 check button
		self.is_verb_1 = BooleanVar()
		Checkbutton(self,
					text = "разворотило",
					variable = self.is_verb_1
					).grid(row = 3, column = 1, sticky = W)
		
		# create verb_2 check button
		self.is_verb_2 = BooleanVar()
		Checkbutton(self,
					text = "воспарить",
					variable = self.is_verb_2
					).grid(row = 3, column = 2, sticky = W)
		
		# create verb_3 check button
		self.is_verb_3 = BooleanVar()
		Checkbutton(self,
					text = "заиндевела",
					variable = self.is_verb_3
					).grid(row = 3, column = 3, sticky = W)
		
		# create verb_4 check button
		self.is_verb_4 = BooleanVar()
		Checkbutton(self,
					text = "вытирать",
					variable = self.is_verb_4
					).grid(row = 3, column = 4, sticky = W)
		
		# create a label for adjectives check buttons
		Label(self,
			  text = "Прилагательные (предызбранные): "
			  ).grid(row = 4, column = 0, sticky = W)
			
		# create adj_1 check button
		self.is_adj_1 = BooleanVar()
		Checkbutton(self,
					text = "приплюснутый",
					variable = self.is_adj_1
					).grid(row = 4, column = 1, sticky = W)
		
		# create adj_2 check button
		self.is_adj_2 = BooleanVar()
		Checkbutton(self,
					text = "растерянный",
					variable = self.is_adj_2
					).grid(row = 4, column = 2, sticky = W)
		
		# create adj_3 check button
		self.is_adj_3 = BooleanVar()
		Checkbutton(self,
					text = "взъерошенный",
					variable = self.is_adj_3
					).grid(row = 4, column = 3, sticky = W)
		
		# create adj_4 check button
		self.is_adj_4 = BooleanVar()
		Checkbutton(self,
					text = "взбалмошный",
					variable = self.is_adj_4
					).grid(row = 4, column = 4, sticky = W)
		
		# create a label for food parts radio buttons
		Label(self,
			  text = "Снедь:"
			  ).grid(row = 5, column = 0, sticky = W)

		# create variable for single, body part
		self.food_part = StringVar()
		self.food_part.set(None)
  
		# create body part radio buttons
		food_parts = ["копчёный окорок", "печёное мясо под сыром", "холодец"]
		column = 1
		for part in food_parts:
			Radiobutton(self,
						text = part,
						variable = self.food_part,
						value = part
						).grid(row = 5, column = column, sticky = W)
			column += 1
		
		# create a label and text entry for a plural noun
		Label(self,
			  text = "Существительное (мн.число):"
			  ).grid(row = 6, column = 0, sticky = W)
		self.noun_ent = Entry(self)
		self.noun_ent.grid(row = 6, column = 1, sticky = W)
		
		# create a submit button
		Button(self,
			   text = "Кликни мну для бредоделки",
			   command = self.tell_story
			   ).grid(row = 7, column = 0, sticky = W)

		self.story_txt = Text(self, width = 125, height = 10, wrap = WORD)
		self.story_txt.grid(row = 8, column = 0, columnspan = 4)
		
	def tell_story(self):
		""" Fill text box with new story based on user input. """
		# get values from the GUI
		person = self.person_ent.get()
		verb = self.verb_ent.get()
		noun = self.noun_ent.get()
		food_part = self.food_part.get()
		if self.is_adj_1.get():
			adj_1 = "приплюснутый"
		if self.is_adj_2.get():
			adj_2 = "растерянный"
		if self.is_adj_3.get():
			adj_3 = "взъерошенный"
		if self.is_adj_3.get():
			adj_4 = "взбалмошный"
		
		if self.is_verb_1.get():
			verb_1 = "разворотило"
		if self.is_verb_2.get():
			verb_2 = "воспарить"
		if self.is_verb_3.get():
			verb_3 = "заиндевела"
		if self.is_verb_4.get():
			verb_4 = "Вытирать"
		

		# create the story
		story = "Сидя на дачном шезлонге с растрескавшейся от солнца краской, "
		story += person + " пожёвывал " + adj_1 + " мундштук."
		story += " Он вспоминал прошлый понедельник, когда " + adj_3 + " курьер"
		story += " вбежал в их отдел и закричал, что половину строящегося объекта "
		if verb_1 :
			story += "просто " + verb_1
		else:
			story += " стёрло с земли"
		story += " после яркой вспышки в небе. Сказать, что вид у присутствующих в зале был "
		if adj_2 :
			story += adj_2 + " и недоверчивый "
		else:
			story += "недоверчивый "
		story += " не было бы большим откровением. Даже "  
		story += adj_4 + " начальник осёкся на половине фразы. "
		story += "\"Впрочем чего это я?\" - подумал " + person
		story += ". \"На работе эти " + noun + ",не хватало ещё и дома о них думать."
		story += " Итак всё время с ними " + verb + ".\""
		story += " И тут он понял, что уже минут 5 облизывает  пересохшие губы, а ведь в холодильнике "
		story += verb_3 + " бутыль морса, и сердце неожиданно было готово "
		if verb_2 :
			story += verb_2 + ". "
		else:
			story += " подпрыгнуть. "
		story += "Резко выбросив тело из шезлонга он торопливо потопал на кухню. " 
		if verb_4 :
			story += verb_4 + " бутыль от осевших мелких капель он не стал, "
		else:
			story += " Ласково огладив бутыль от конденсата и "
		story += " поколебавшись немного, решил, что негоже не подкрепиться и "
		story += "достал с полочки ещё и "
		if food_part:
			story += food_part + ". "
		else:
			story += " рулетик с маком. "
		story += " Жизнь налаживалась."
		
		# display the story
		self.story_txt.delete(0.0, END)
		self.story_txt.insert(0.0, story)
		
# main
root = Tk()
root.title("Crazy Tales")
app = Application(root)
root.mainloop()