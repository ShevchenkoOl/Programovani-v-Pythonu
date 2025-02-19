#------------------------------Lekce 4 Objektově orientované programování v Pythonu 
#---------------------------------------Objekty
class Employee:
    def __init__(self, name, position, holiday_entitlement):      # __init__ Метод __init__ в Python — это специальный метод, который называется конструктором класса. Он вызывается автоматически при создании нового объекта (экземпляра) этого класса. Основная цель __init__ — инициализация объекта, то есть присваивание начальных значений его атрибутам
        self.name = name                                          # self self — это первый параметр всех методов класса в Python, который ссылается на текущий экземпляр объекта, для которого вызывается метод. Это своего рода указатель на сам объект.
        self.position = position
        self.holiday_entitlement = holiday_entitlement
    def get__info(self):
        return f"{self.name} pracuje na posice {self.position}." 
    
frantisek = Employee("Frantisek Novak", "konstrukter", 25)
klara = Employee("Klara Navo", "konstrukterka", 25)

print(frantisek.name)           # Frantisek Novak
print(frantisek.get__info())    # Frantisek Novak pracuje na posice konstrukter.
print(klara.get__info())        # Klara Navo pracuje na posice konstrukterka.

#-----------------------------------Cvičení 1: Balík
class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state
    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg, je ve stavu {self.state}."
    def delivery_price(self):
        if self.weight <= 10:
            return 129
        elif self.weight <= 20:
            return 159
        else:
            return 359
        
balik1 = Package("Ulice Smetanova 123", 2.5, "doručen")
balik2 = Package("Ulice Smetanova 123", 15.5, "doručen")
    
print(balik1.get_info())       # Balík na adresu Ulice Smetanova 123 má hmotnost 2.5 je ve stavu doručen.   

print(f"Cena přepravy balíku 1: {balik1.delivery_price()} Kč")  # Cena přepravy balíku 1: 129 Kč
print(f"Cena přepravy balíku 2: {balik2.delivery_price()} Kč")  # Cena přepravy balíku 2: 159 Kč



#-----------------------------------Bonusy Cvičení 2: Kniha

class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price
    def get_info(self):
        return f"Kniha '{self.title}' obsahuje {self.pages} stran a cena je {self.price} Kč."
    def get_time_to_read(self, timer = 4):
        totat_time = self.pages * timer
        hours = totat_time // 60
        min = totat_time % 60
        return f"Kniha '{self.title}' budete číst za {hours} hodin a {min} minut."
        
kniha1 = Book("Jednotlivý záběr", 150, 29.99)
print(kniha1.get_time_to_read())      # Kniha 'Jednotlivý záběr' budete číst za 10 hodin a 0 minut.