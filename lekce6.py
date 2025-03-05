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
#        listManager.append(item)
#             # return f"Naši pracovníci, kteří pracují na pozici manažera: {item}
# return f"Naši pracovníci, kteří pracují na pozici manažera: {listManager}"
# for manager in listManager:
#     print(manager)
