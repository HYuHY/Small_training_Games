#Autodiller
#Demonstrates the input and some calculation functions


car_cost = float(input("Введите стоимость автомобиля без наценок:\n"))
car_tax = car_cost * 0.16
car_registration = car_cost * 0.08
car_agent = 200
car_delivery = 250
print("\n\nНалог на данный автомобиль составляет: ", car_tax)
print("\nРегистрационный сбор на данный"\
      + " автомобиль составляет: ", car_registration)
print("\nАгентский сбор на данный автомобиль составляет: ", car_agent)
print("\nЦена доставки по месту для"\
      + " данного автомобиля составляет: ", car_delivery)

car_cost_sum = car_cost + car_tax + car_registration + car_agent + car_delivery

print("\n\n\nОкончательная цена автомобиля составляет: ", car_cost_sum)
input("\nДля закрытия окна программы нажмите Enter")
