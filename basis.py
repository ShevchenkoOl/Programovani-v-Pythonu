# a = True
# b = []
# print(type(a))      # <class 'bool'>
# print(type(b))      # <class 'list'>
# print(type('alex')) # <class 'str'>
# print(type(3))      # <class 'int'>
# print(type(3.5))    # <class 'float'>


# text = 'Here is some random text'
# print(text.find('h'))  # -1
# print(text.find('H'))  # 0 - toto je indexové číslo, kde se dané písmeno nachází
# text2 = '5'
# text2.rjust(8)       #         5
# text2.rjust(4,'.')   # ...5
# text2.center(5, '*') # **5**



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
