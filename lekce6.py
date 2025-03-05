#------------------------------------------------------Objektově orientované programování v Pythonu
#-------------------------------------------------------------------Datové třídy

# Когда мы определяем класс для хранения некоторых атрибутов, выглядит это примерно так:
# class Person():
#     def __init__(self, first_name, last_name, age, job):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.job = job

# перепишем код с использованием dataclasses
# from dataclasses import dataclass
# @dataclass
# class Person:
#      first_name: str
#      last_name: str
#      age: int
#      job: str

#---------------------------------------Cvičení: Balík jako datová třída
# from dataclasses import dataclass

# @dataclass
# class Package:
#       address: str
#       weight: float
#       state: str
      
#       def __str__(self):
#           return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

# balik1 = Package("Vodickova 2754/21", 23.5, "doruceno")
# print(balik1)


#-----------------------------------------------------Funkce pro práci s objekty
# ------------------------------------------Funkce isinstance()
# from dataclasses import dataclass

# @dataclass
# class Employee:
#               name: str
#               position: str

#               def __str__(self):
#                   return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

# @dataclass
# class Manager(Employee):
#              car: str
        
#              def __str__(self):
#                   base_info = super().__str__()  # Используем метод из родителя
#                   return f"{base_info} Má auto {self.car}."
# novak = Employee("Jan Novak", "recepce")        
# marian = Manager("Marian Přísný","meneger", "Škoda Octavia 1.5 TSI")
# frantisek = Employee("František Novák", "konstruktér")
# kate = Manager("Katerina Smela","meneger", "Škoda Octavia 1.5 TSI")

# personal = [novak, marian, frantisek, kate]
# listManager = []

# for item in personal:
#     if isinstance(item, Manager):
#        listManager.append(item.name)
#             # return f"Naši pracovníci, kteří pracují na pozici manažera: {item}
# print(f"Naši pracovníci, kteří pracují na pozici manažera: {listManager}")
# for manager in listManager:
#     print(manager)


#---------------------------------------Cvičení 1: Celková hodnota balíků
# from dataclasses import dataclass

# @dataclass
# class Package:
#     address: str
#     weight: float
#     state: str

#     def __str__(self):
#         return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

# @dataclass
# class ValuablePackage(Package):
#     value: int

#     def __str__(self):
#         return super().__str__() + f" Balík má hodnotu {self.value} Kč."

# # Создание объектов
# package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
# package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
# package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)

# package_list = [package_1, package_2, package_3]

# # Вычисление общей стоимости ценных посылок
# total_value = 0

# for package in package_list:
#     # Проверяем наличие атрибута value
#     if hasattr(package, 'value'):
#         total_value += package.value

# print(f"Celková hodnota cenných balíků v autě: {total_value} Kč")


#---------------------------------------Bonus Cvičení 2: Celková hodnota balíků podruhé
# Определение классов
# from dataclasses import dataclass

# @dataclass
# class Package:
#     address: str
#     weight: float
#     state: str

#     def __str__(self):
#         return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

# @dataclass
# class ValuablePackage(Package):
#     value: int

#     def __str__(self):
#         return super().__str__() + f" Balík má hodnotu {self.value} Kč."

# # Создание объектов
# package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
# package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
# package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)
# package_4 = ValuablePackage("Privet Drive 4", 2.3, "doručen", 8000)  # Новый доставленный ценный пакет

# package_list = [package_1, package_2, package_3, package_4]

# # Вычисление общей стоимости недоставленных ценных посылок
# total_value = 0

# for package in package_list:
#     # Проверяем наличие атрибута value и состояние "nedoručen"
#     if hasattr(package, 'value') and getattr(package, 'state', '') == "nedoručen":
#         total_value += package.value

# print(f"Celková hodnota cenných balíků v autě: {total_value} Kč")


#---------------------------------------Bonus Cvičení 3: Vypravěči
# Определение классов
# class Item:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price

#     def get_time_to_read(self):
#         pass

# class Book(Item):
#     def __init__(self, title, price, pages):
#         super().__init__(title, price)
#         self.pages = pages

#     def get_info(self):
#         return f"Kniha '{self.title}' má {self.pages} stran a stojí {self.price} Kč."

#     def get_time_to_read(self):
#         return self.pages * 4 / 60

# class AudioBook(Item):
#     def __init__(self, title, price, duration_in_hours, narrator):
#         super().__init__(title, price)
#         self.duration_in_hours = duration_in_hours
#         self.narrator = narrator

#     def get_time_to_read(self):
#         return self.duration_in_hours

# # Заданное имя диктора
# favourite_narrator = "Zbyšek Horák"

# # Создание объектов
# item_1 = AudioBook("Problém tří těles", 299, 14.4, "Zbyšek Horák")
# item_2 = Book("Kadet Hornblower", 399, 242)
# item_3 = AudioBook("Odysseus", 389, 13.7, "Lukáš Hlavica")

# all_items = [item_1, item_2, item_3]

# # Поиск и вывод аудиокниг с нужным диктором
# print("Audioknihy s oblíbeným vypravěčem:")

# for item in all_items:
#     # Проверяем наличие атрибута narrator и его совпадение с favourite_narrator
#     if getattr(item, 'narrator', None) == favourite_narrator:
#         print(item.title)