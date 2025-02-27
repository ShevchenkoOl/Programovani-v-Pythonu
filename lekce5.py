#------------------------------Lekce 4 Objektově orientované programování v Pythonu
#------------------------------------Dědičnost
# Наследственность (Inheritance) — это один из ключевых принципов объектно-ориентированного программирования (ООП), который позволяет создавать новый класс на основе уже существующего. Новый класс (называется дочерним или производным) наследует свойства (атрибуты) и методы родительского класса, но может добавлять свои или изменять унаследованные.
# class Employee:
#     def __init__(self, name, position, holiday_entitlement):
#         self.name = name
#         self.position = position
#         self.holiday_entitlement = holiday_entitlement

#     def __str__(self):
#         return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

#     def take_holiday(self, days):
#         if self.holiday_entitlement >= days:
#             self.holiday_entitlement -= days
#             return f"Užij si to."
#         else:
#             return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

# class Manager(Employee):
#     def __init__(self, name, holiday_entitlement, subordinates, car):
#         # Вызываем конструктор родительского класса с тремя аргументами
#         super().__init__(name, "manažer(ka)", holiday_entitlement)
#         self.subordinates = subordinates
#         self.car = car

#     def __str__(self):
#         # base_info = super().__str__()  # Используем метод из родителя
#         # return f"{base_info} Má {self.subordinates} podřízené a auto {self.car}."
#         return super().__str__() + f" Má {self.subordinates} podřízené a auto {self.car}."

# # Новый класс ProjectManager, наследник Manager
# class ProjectManager(Manager):
#     def __init__(self, name, holiday_entitlement, subordinates, car, projects):
#         super().__init__(name, holiday_entitlement, subordinates, car)
#         self.projects = projects
        
# marian = Manager("Marian Přísný", 25, 2, "Škoda Octavia 1.5 TSI")
# jana = ProjectManager("Jana Pečlivá", 30, 3, "BMW X3", ["Projekt A", "Projekt B"])
# print(marian) # Zaměstnanec Marian Přísný pracuje na pozici manažer(ka). Má 2 podřízené a auto Škoda Octavia 1.5 TSI.
# print(jana)   # Zaměstnanec Jana Pečlivá pracuje na pozici manažer(ka). Má 3 podřízené a auto BMW X3.

# #-----------------------------------Cvičení 1: Cenný balík
# class Package:
#     def __init__(self, address, weight, state):
#         self.address = address
#         self.weight = weight
#         self.state = state

#     def __str__(self):
#         return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

#     def delivery_price(self):
#         if self.weight < 10:
#             return 129
#         elif self.weight < 20:
#             return 159
#         else:
#             return 359

# class ValuablePackage(Package):
#     def __init__(self, address, weight, state, value):
#         super().__init__(address, weight, state)
#         self.value = value
    
#     def __str__(self):
#         return super().__str__() + f" Jeho cena je {self.value}"

# balik1 = ValuablePackage("Ulice Smetanova 123", 2.5, "doručen", 3256)

# print(balik1) # Balík na adresu Ulice Smetanova 123 má hmotnost 2.5 kg a je ve stavu doručen. Jeho cena je 3256


#-----------------------------------Cvičení 2: Cena přepravy
# class Package:
#     def __init__(self, address, weight, state):
#         self.address = address
#         self.weight = weight
#         self.state = state

#     def __str__(self):
#         return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

#     def delivery_price(self):
#         if self.weight < 10:
#             return 129
#         elif self.weight < 20:
#             return 159
#         else:
#             return 359

# class ValuablePackage(Package):
#     def __init__(self, address, weight, state, value):
#         super().__init__(address, weight, state)
#         self.value = value
    
#     def __str__(self):
#         return super().__str__() + f" Jeho cena je {self.value}"
    
#     def delivery_price(self):
#         return super().delivery_price() + self.value * 0.05
        
# balik1 = ValuablePackage("Ulice Smetanova 123", 0.25, "doručen", 500)
# print(balik1.delivery_price()) # 154.0


#-----------------------------------Bonusy Cvičení 3: Jízdenky a letenky
# class Ticket:
#     def __init__(self, basic_price, seat_number):
#         self.basic_price = basic_price
#         self.seat_number = seat_number
#     def __str__(self):
#         return f"Cena letenky je: {self.basic_price} kč, a vaše sedadlo čislo: {self.seat_number}"
  
# class TrainTicket(Ticket):
#     def __init__(self, basic_price, seat_number, fare_class):
#         super().__init__(basic_price, seat_number)  
#         self.fare_class = fare_class
    
#     def get_price(self):
#         if self.fare_class == "economy":
#             return f"Třída, kterou jste si vybrali, je economy. {super().__str__()}"
#         else:
#             return f"Třída, kterou jste si vybrali, je business. Cena letenky je: {self.basic_price * 1.3} kč, a vaše sedadlo čislo: {self.seat_number}"

# class PlaneTicket(TrainTicket):
#     def __init__(self, basic_price, seat_number, fare_class, checkout_luggages):
#         super().__init__(basic_price, seat_number, fare_class)
#         self.checkout_luggages = checkout_luggages
    
#     def get_price(self):
#         if self.fare_class == "economy":
#             return f"Třída, kterou jste si vybrali, je economy. Cena letenky je: {self.basic_price + self.checkout_luggages * 2000}  kč, a vaše sedadlo čislo: {self.seat_number}"
#         else:
#             return f"Třída, kterou jste si vybrali, je business. Cena letenky je: {self.basic_price * 1.5 + self.checkout_luggages * 2000} kč, a vaše sedadlo čislo: {self.seat_number}"



# ticket1 = TrainTicket(1000, 12, "economy")
# ticket2 = TrainTicket(1000, 15, "business")

# ticket3 = PlaneTicket(150, 7, "economy", 0)
# ticket4 = PlaneTicket(150, 7, "business", 0)


# ticket5 = PlaneTicket(6000, 3, "economy", 1)
# ticket6 = PlaneTicket(6000, 3, "business", 1)

# total_price = ticket1.get_price() + ticket3.get_price()

# print(ticket1.get_price()) # Třída, kterou jste si vybrali, je economy. Cena letenky je: 1000 kč, a vaše sedadlo čislo: 12
# print(ticket2.get_price()) # Třída, kterou jste si vybrali, je business. Cena letenky je: 1300.0 kč, a vaše sedadlo čislo: 15
# print(ticket3.get_price()) # Třída, kterou jste si vybrali, je economy. Cena letenky je: 150  kč, a vaše sedadlo čislo: 7
# print(ticket4.get_price()) # Třída, kterou jste si vybrali, je business. Cena letenky je: 225.0 kč, a vaše sedadlo čislo: 7
# print(ticket5.get_price()) # Třída, kterou jste si vybrali, je economy. Cena letenky je: 8000  kč, a vaše sedadlo čislo: 3
# print(ticket6.get_price()) # Třída, kterou jste si vybrali, je business. Cena letenky je: 11000.0 kč, a vaše sedadlo čislo: 3
# print(total_price)


#-----------------------------------Bonusy Cvičení 4: Audioknihy
