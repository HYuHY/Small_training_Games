# Генератор персонажей
#
# Пользователю предоставляется некоторое число пунктов, которые можно
# распределить между 4мя характеристиками: сила, здоровье, мудрость и
# ловкость. Пользователь должен иметь возможность как брать, так и 
# возвращать пункты из пула в характеристики.
#

stats_point = 30
stats = {"Сила": 0, "Ловкость": 0, "Здоровье": 0, "Мудрость": 0}
options = ("""
    Для выбора действия нажмите соответствующую клавишу :
    0\tВыйти из программы
    1\tИзменить параметр 'Сила'
    2\tИзменить параметр 'Ловкость'
    3\tИзменить параметр 'Здоровье'
    4\tИзменить параметр 'Мудрость'\n """)
options_pool = ('0','1','2','3','4')
		
change_help = (
"""
Чтобы изменить характеристику персонажа, введите положительное 
число для увеличения характеристики или отрицательное - для уменьшения.
Например:  ввод "+10" (без кавычек) поднимает ранее выбранную 
характеристику на 10, а "-3" - уменьшает на 3 пункта. Суммарно вы 
можете потратить на персонажа не более 30 пунктов характеристик.
Для выхода в меню выбора характеристики введите '0'.
""")
		
		
choice = None
while choice !=0 :
	while str(choice) not in options_pool:
		if choice!=None :
			print("Такой опции в программе не предусмотрено\n")
		print("Осталось пунктов характеристик: ", stats_point)
		print("Сейчас характеристики персонажа следующие:\n")
		print(	'Сила ', stats['Сила'], 
				'\tЛовкость ', stats['Ловкость'],
				'\tЗдоровье ', stats['Здоровье'], 
				'\tМудрость ', stats['Мудрость'])
		choice = input(options)
		if choice.isdecimal():
			choice = int(choice)
	
	choice = int(choice)
	if choice == 1:
		stats_key = "Сила"
	elif choice == 2:
		stats_key = "Ловкость"
	elif choice == 3:
		stats_key = "Здоровье"
	elif choice == 4:
		stats_key = "Мудрость"
	elif choice == 0:
		print ("Спасибо за использование программы. До свидания.")
		
	change_stat = "init"
	correct_input = False
	while change_stat != 0 and choice != 0:
		print(change_help)
		print("Осталось пунктов характеристик: ", stats_point)
		print("Текущая величина характеристики ", stats_key, 
				stats[stats_key])

		change_stat = input("Введите величину изменения характеристики ")
		
		while correct_input == False :
			if change_stat[0] == '+' or change_stat[0] == '-':
				if change_stat[1:].isdecimal() == False :
					correct_input = False
				else :
					correct_input = True
			elif change_stat.isdecimal() == False :
				correct_input = False
			else :
				correct_input = True
			if correct_input == False :
				change_stat = input("Введите величину изменения характеристики ")

		if change_stat != "init" :
			change_stat = int(change_stat)
			
		if (change_stat > 0 and change_stat <= stats_point) or \
			(change_stat < 0 and abs(change_stat) <= stats[stats_key]):
			stats[stats_key] = stats[stats_key] + change_stat
			stats_point -= change_stat
		elif change_stat == 0:
			print("\nИзменения сохранены")
		else :
			print("\nНевозможно изменить характеристику на такую величину")
	
	if choice != 0:
		choice = None

input("Нажмите Enter для выхода из программы")
