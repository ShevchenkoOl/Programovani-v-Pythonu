# a = True
# b = []
# print(type(a))      # <class 'bool'>
# print(type(b))      # <class 'list'>
# print(type('alex')) # <class 'str'>
# print(type(3))      # <class 'int'>
# print(type(3.5))    # <class 'float'>
'''
Aritmetické operátory
operátor přiřazení = 
rovnat se ==
ne rovna se !=
větší než > 
menší než <
větší nebo rovno >=
menší nebo rovno <=
sčítání: +
odčítání: -
násobení: *
dělení: /
mocnění: **                возводит в степень 2 ** 3 (2 в 3 степени) zvyšuje na sílu 2 ** 3 (2 na 3)
celočíselné dělení: //     делит числа без остатка 7 // 2 = 3
zbytek po dělení: %        vzít zbytek dělení 7 / 2, abyste dostali celé číslo 3 a zbyde nám 1 (2*3=6 7-6=1)

print(f'studentské vstupné činí {koruny} kč') - F-řetězce (formátované řetězce) umožňují vložit hodnoty proměnných přímo do řetězce bude to na lekce 4
print("Divadlo Pěst na oko \n",  "Vítejte v online rezervaci vstupenek \n", "Pro vstup do systému je potřeba registrace \n")
'''

# text = 'Here is some random text'
# print(text.find('h'))  # -1
# print(text.find('H'))  # 0 - toto je indexové číslo, kde se dané písmeno nachází
# text2 = '5'
# text2.rjust(8)       #         5
# text2.rjust(4,'.')   # ...5
# text2.center(5, '*') # **5**
print(list("Ahoj"))   # ['A', 'h', 'o', 'j']
print("slovo jese odno slovo i tak dalee".split())  # ['slovo', 'jese', 'odno', 'slovo', 'i', 'tak', 'dalee']
print("slovo / jese odno slovo i / tak dalee".split("/")) # ['slovo ', ' jese odno slovo i ', ' tak dalee']



# radky = [
#     [2001, 7.8],
#     [2002, 8.7],
#     [2003, 8.2],
#     [2004, 7.8],
#     [2005, 7.7],
#     [2006, 8.2],
#     [2007, 9.1],
#     [2008, 8.9],
#     [2009, 8.4],
#     [2010, 7.2]
# ]
# print(radky[-1]) # [2010, 7.2] - posledni prvek seznamu
# print(" ".join(["John", "Peter", "Vicky"]))  # John Peter Vicky
# print(" @".join(["John", "Peter", "Vicky"])) # John @Peter @Vicky
# print(random.shuffle(radky))  # náhodně mění pozici položek seznamu
# radky.append([2012, 8.6])  # přidá do seznamu radky






# #---------------Numbers
# import random
# print(random.randint(0, 36))  # náhodné číslo od o do 36




#--------------Vlastní funkce
# def greet_user():  # def - definici funkce, nazev_funkce(parametry)
#     print("Ahoj!") # tělo funkce 

# greet_user()       # volani funkce
#                    # po vyvolání funkce se spustí print()  a zobrazí se konzole 'Ahoj'
# def sum_two_numbers(a, b):
#     return a + b

# suma_cisel = sum_two_numbers(3, 5)
# print(suma_cisel)   # 8


# Nepovinné parametry a typování (annotation)
# Anotace parametrů funkce není povinná, pouze ukazuje vývojáři, jaký typ parametru funkce chce vidět.
# def test(number: int, stringa: str = "5"):  # nebo isOnline: boolean = True atd.
#     print(number * stringa)
# test(5) # pokud nepředáme druhý parametr, bude to automaticky to, co je uvedeno v parametrech  - 55555
# test(5, '*') # *****


# funkci lze také volat iterací přes seznam:
# def spocitej_pokutu(a, b):
#   ...........

# vazeni = [
#     [4, 30],
#     [2, 19],
#     [3, 29],
#     [3, 27],
#     [5, 53],
#     [5, 51],
#     [2, 20],
# ]

# for index in vazeni:
#     spocitej_pokutu(index[0], index[1])
