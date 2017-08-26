#Счёт
#
#Считает по вводу пользователя. Принимает начало и конец отсчёта, интервал

start = int(input("\nВведите начало счёта "))
finish = int(input("\nВведите конец счёта "))
interval = int(input("\nВведите интервал счёта "))

for i in range(start, finish, interval):
	print(i, end = " ")

input("\nнажмите Enter для выхода из программы")