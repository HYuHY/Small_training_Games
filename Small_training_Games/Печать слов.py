# Вывод слов в случайном порядке
#
# Программа выводит заданный список слов в случайном порядке.                  
# Все слова из списка без повторов печатаются на экране
# 

import random
WORDS = ("генератор", "тетраграмматон", "алиллуя", "иллюзия", "таран",
		"перестрелка", "гигабайт", "генератор")
		
list_words = list(WORDS)
list_random = []
while len(list_words)>0 :
	random_word = random.choice(list_words)
	if random_word not in list_random :
		list_random.append(random_word)
	while random_word in list_words :
		del_position = list_words.index(random_word)
		list_words.pop(del_position)

print(list_random)
input("Нажмите Enter для выхода из программы")

