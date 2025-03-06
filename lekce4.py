#------------------------------Lekce 4 Objektově orientované programování v Pythonu
# Základní principy (myšlenky) OOP: 1. zapouzdření (Инкапсуляция, Encapsulation) - omezení přístupu ke komponentám (metodám a proměnným), které tvoří objekt. Zapouzdření zpřístupňuje některé komponenty pouze v rámci třídy.
# Одиночное подчеркивание в начале имени атрибута говорит о том, что переменная или метод не предназначен для использования вне методов класса, однако атрибут доступен по этому имени
# class A:
#         def _private(self):
#         print("Это приватный метод!")
# a = A()
# a._private()
# Двойное подчеркивание в начале имени атрибута даёт большую защиту: атрибут становится недоступным по этому имени.
# class B:
#        def __private(self):
#       print("Это приватный метод!")
# b = B()
# b.__private()
#                                   2. dědičnost (Inheritance)- dědičnost znamená, že podřízená třída obsahuje všechny atributy nadřazené třídy, i když některé z nich mohou být v podřízené třídě přepsány nebo přidány.
#                                   3. polymorfismus -pracovat s objekty různých tříd jednotným způsobem

#---------------------------------------Objekty a třídy
# class Employee:
#     def __init__(self, name, position, holiday_entitlement):      # __init__ Метод __init__ в Python — это специальный метод, который называется конструктором класса. Он вызывается автоматически при создании нового объекта (экземпляра) этого класса. Основная цель __init__ — инициализация объекта, то есть присваивание начальных значений его атрибутам
#         self.name = name                                          # self — это первый параметр всех методов класса в Python, который ссылается на текущий экземпляр объекта, для которого вызывается метод. Это своего рода указатель на сам объект.
#         self.position = position
#         self.holiday_entitlement = holiday_entitlement
#     def get__info(self):
#         return f"{self.name} pracuje na posice {self.position}." 
    
# frantisek = Employee("Frantisek Novak", "konstrukter", 25)
# klara = Employee("Klara Navo", "konstrukterka", 25)

# print(frantisek.name)           # Frantisek Novak
# print(frantisek.get__info())    # Frantisek Novak pracuje na posice konstrukter.
# print(klara.get__info())        # Klara Navo pracuje na posice konstrukterka.


# Příklady obslužných metod (začátek a konec se dvěma podtržítky):
# __init__ — inicializace objektu (spuštění při vytváření).   — инициализация объекта (запуск при создании).
# __str__ — řetězcová reprezentace objektu (jak bude vypadat při `print()`) —  строковое представление объекта (как будет выглядеть при `print()`).
# __len__ — délka objektu (funguje s funkcí `len()`), používá se pouze pro typ int (číslo) — длина объекта (работает с функцией `len()`), используется только для типа int (число).
# __add__ — přidání objektů (funguje s `+`), matematická metoda — сложение объектов (работает с `+`).

#------------------------Příklady použití těchto metod
# class Employee:
#     def __init__(self, name, position, holiday_entitlement):
#         self.name = name
#         self.position = position
#         self.holiday_entitlement = holiday_entitlement

#     def __str__(self):
#         return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
        
#     # def get_info(self):
#     #     return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    
#     def __len__(self):
#         return self.holiday_entitlement
        
#     def take_holiday(self, days):
#         if self.holiday_entitlement >= days:
#            self.holiday_entitlement -= days
#            return f"Užij si to."
#         else:
#             return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

# frantisek = Employee("Frantisek Novak", "developer", 25)
# print(frantisek.take_holiday(30)) # Bohužel už máš nárok jen na 25 dní.
# print(frantisek)    # Zaměstnanec Frantisek Novak pracuje na pozici developer.
# print(len(frantisek)) # 25

#-----------------------------------Cvičení 1: Balík
# class Package:
#     def __init__(self, address, weight, state):
#         self.address = address
#         self.weight = weight
#         self.state = state
#     def get_info(self):
#         return f"Balík na adresu {self.address} má hmotnost {self.weight} kg, je ve stavu {self.state}."
#     def delivery_price(self):
#         if self.weight <= 10:
#             return 129
#         elif self.weight <= 20:
#             return 159
#         else:
#             return 359
        
# balik1 = Package("Ulice Smetanova 123", 2.5, "doručen")
# balik2 = Package("Ulice Smetanova 123", 15.5, "doručen")
    
# print(balik1.get_info())       # Balík na adresu Ulice Smetanova 123 má hmotnost 2.5 je ve stavu doručen.   

# print(f"Cena přepravy balíku 1: {balik1.delivery_price()} Kč")  # Cena přepravy balíku 1: 129 Kč
# print(f"Cena přepravy balíku 2: {balik2.delivery_price()} Kč")  # Cena přepravy balíku 2: 159 Kč



#-----------------------------------Bonusy Cvičení 2: Kniha
# class Book:
#     def __init__(self, title, pages, price):
#         self.title = title
#         self.pages = pages
#         self.price = price
#     def get_info(self):
#         return f"Kniha '{self.title}' obsahuje {self.pages} stran a cena je {self.price} Kč."
#     def get_time_to_read(self, timer = 4):    # timer = 4 - nepovinný parametr
#         totat_time = self.pages * timer
#         hours = totat_time // 60
#         min = totat_time % 60
#         return f"Kniha '{self.title}' budete číst za {hours} hodin a {min} minut."
        
# kniha1 = Book("Jednotlivý záběr", 150, 29.99)
# print(kniha1.get_time_to_read())      # Kniha 'Jednotlivý záběr' budete číst za 10 hodin a 0 minut.


#----------------------------------- Cvičení 1: Balík podruhé
# class Package:
#     def __init__(self, address, weight, state):
#         self.address = address
#         self.weight = weight
#         self.state = state
    
#     def __str__(self):   # přejmenuj metodu get_info() na __str__() a vyzkoušej, jestli nyní stačí k získání informací o balíku funkce print().
#         return(f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state}")
    
#     def deliver(self):   # bod 2
#         if self.state == "doručen":
#             return "Balík již byl doručen"
#         else:
#             self.state = "doručen"
#             return "Doručení uloženo"
    
#     def delivery_price(self):
#         if self.weight <= 10:
#             return f"Cena přepravy balíku je 129 cze"
#         elif self.weight < 20:
#             return f"Cena přepravy balíku je 159 cze"
#         else:
#             return f"Cena přepravy balíku je 359 cze"
            
# balik1 = Package("Krakovská 583/9, Praha", 0.25, "nedoručen")
# balik2 = Package("Olšanská 80, Praha", 20.95, "nedoručen")
# balik3 = Package("Sokolska 36, Olomouc", 11.25, "doručen")

# print(balik1, balik2, balik3)   # Balík na adresu Krakovská 583/9, Praha má hmotnost 0.25 kg je ve stavu nedoručen Balík na adresu Olšanská 80, Praha má hmotnost 20.95 kg je ve stavu nedoručen Balík na adresu Sokolska 36, Olomouc má hmotnost 11.25 kg je ve stavu doručen

# print(balik1.deliver(), balik1)  # Doručení uloženo Balík na adresu Krakovská 583/9, Praha má hmotnost 0.25 kg je ve stavu doručen
# print(balik3.deliver(), balik3) # Balík již byl doručen Balík na adresu Sokolska 36, Olomouc má hmotnost 11.25 kg je ve stavu doručen


#-----------------------------------Bonusy Cvičení 2: Kniha podruhé
# class Book:
    
#     def __init__(self, title, pages, price, sold, cost):
#         self.title = title
#         self.pages = pages
#         self.price = price
#         self.sold = sold
#         self.cost = cost
    
#     def __str__(self):
#         return f'Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč'
    
#     def get_time_to_read(self, page_minutes = 4):
#         totat_time = self.pages * page_minutes
#         hod = totat_time // 60
#         min = totat_time % 60
#         return f'Přečtení knihy {self.title} vám zabere {hod} hodiny a {min} minut.'
    
#     def profit(self):
#         return (self.price - self.cost) * self.sold

#     def rating(self):
#         if self.sold < 50000:
#             return "propadák"
#         elif self.sold < 500000:
#             return "průměr"
#         else:
#             return "bestseller"
        
# book_1 = Book("Day of the Wipers", 528, 646, 340000, 260)
# print(f"Zisk z prodeje knihy je {book_1.profit()} Kč.")     # Zisk z prodeje knihy je 131240000 Kč.
# print(f"Kniha je {book_1.rating()}.")  # Kniha je průměr.


#-----------------------------------Bonusy Cvičení 3: Zkušební doba
# class Employee:
#     def __init__(self, name, position, probation_period):
#         self.name = name
#         self.position = position
#         self.probation_period = probation_period

#     def __str__(self):
#         if self.probation_period == "Zkušební doba":
#            return f"Zaměstnanec {self.name} pracuje na pozici {self.position}. Je ve zkušební době"
#         return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    
# frantisek = Employee("Frantisek Novak", "developer", "")
# elvira = Employee("Elvira Vesela", "front-desck", "Zkušební doba")
# print(frantisek)  # Zaměstnanec Frantisek Novak pracuje na pozici developer.
# print(elvira)     # Zaměstnanec Elvira Vesela pracuje na pozici front-desck. Je ve zkušební době


#-----------------------------------Bonusy Cvičení 4: Seznam balíků
# class Package:
#     def __init__(self, address, weight, state):
#         self.address = address
#         self.weight = weight
#         self.state = state
    
#     def delivery_price(self):
#         if self.weight < 10:
#             return 129
#         if self.weight < 20:
#             return 159
#         return 359
    
#     def deliver(self):
#         if self.state == "doručen":
#             return "Balík již byl doručen"
#         else:
#             self.state = "doručen"
#             return "Doručení uloženo"

#     def __str__(self):
#         return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."
    

# package_1 = Package("Grimmauldovo náměstí 11", 15, "nedoručen")
# package_2 = Package("Godrikův důl 47", 3, "nedoručen")
# package_3 = Package("Vydrník svatého Drába 13", 0.5, "nedoručen")
# package_list = [package_1, package_2, package_3]

# total_weight = 0
# total_price = 0

# for item in package_list:
#     total_weight += item.weight
#     total_price += item.delivery_price()
    
# print(f'Celková hmotnost všech balíků je: {total_weight} kg')        # Celková hmotnost všech balíků je: 18.5 kg
# print(f"Celková cena za přepravu všech balíků je {total_price} Kč.") # Celková cena za přepravu všech balíků je 417 Kč.



#---------------------------------------------------------Soukromé atributy a vlastnosti
# Dekorátor @property nám umožňuje vytvářet vlastnosti objektů a definovat přístupové metody pro atributy tříd. Je to velmi užitečné, když chceme skrýt detaily implementace atributů a poskytnout pohodlné rozhraní pro přístup k nim.
# Декоратор @property позволяет нам создавать свойства объектов и определять методы доступа к атрибутам класса. Он очень полезен, когда мы хотим скрыть детали реализации атрибутов и предоставить удобный интерфейс для доступа к ним.
# Příklad 1: Vytvoření vlastnosti objektu @property decorator nám umožňuje vytvářet vlastnosti objektu. Můžeme například vytvořit třídu Rectangle s atributy width a height. Poté můžeme definovat metodu oblasti, která vrátí oblast obdélníku.
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     @property
#     def area(self):
#         return self.width * self.height

# w = int(input("Prosím zadejte šířku obdélníku: "))
# h = int(input("Prosím zadejte výšku obdélníku: "))

# print(f"Plocha obdélníku je: {Rectangle(w, h).area} cm") # Prosím zadejte šířku obdélníku: 5
#                                                          # Prosím zadejte výšku obdélníku: 10
#                                                          # Plocha obdélníku je: 50 cm


# Příklad 2: Použití metod přístupu k atributům. Dekorátor @property lze také použít k definování přístupových metod pro atributy třídy. Můžeme například definovat třídu Osoba s atributy jména a věku. Poté můžeme definovat metody přístupového objektu jména a věku pomocí dekorátorů @property.getter a @property.setter.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return self.name + " " + self.age
#     @property
#     def name(self):
#         return self._name     # omezit přístup (soukromny atribut)
    
#     @name.setter              # se používají k nastavení hodnot atributů.
#     def name(self, value):
#         self._name = value
    
#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         self._age = value

# name = input("Prosím zadejte svoje jmeno: ")
# age = input("Prosím zadejte svůj věk: ")
# p = Person(name, age)
# print(p) # Prosím zadejte svoje jmeno: Alex
#          # Prosím zadejte svůj věk: 65
#          # Alex 65
         
# p.name = "Oleg"
# p.age = "15"
# print(p)  # Oleg 15



# ---------------------------------------------------------------------- Cvičení: Balík potřetí
# class Employee:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     @property
#     def _name_length(self):
#         return len(self.first_name + self.last_name)

#     @property
#     def business_card_data(self):
#         if self._name_length < 20:
#             return f"{self.first_name} {self.last_name}"
#         else:
#             return f"{self.first_name[0]}. {self.last_name}"

# p = Employee("Alex", "Shilov")
# print(p.business_card_data) # Alex Shilov
         
         
# p.first_name = "Jan"
# p.last_name = "Novak"
# print(p.business_card_data)  # Jan Novak
