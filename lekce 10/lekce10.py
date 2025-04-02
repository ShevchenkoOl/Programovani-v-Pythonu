# ------------------------ Lekce 10 Obsluha výjimek, Chyby v programu
# def is_odd(number):
#     return number % 2 == 0
# assert is_odd(4) == False  # Теперь проверяем корректно
# assert is_odd(5) == True  # Проверяем нечетное число
# assert используется для проверки утверждений (предположений) в коде. Если выражение после assert оказывается ложным, то программа выдаст ошибку (AssertionError) и прекратит выполнение.


# -----------------------------Výjimky a krokování start deburging
# lines = []
# with open("smeny.txt", encoding="utf-8") as file:
#     for line in file:
#         lines.append(line)
# avg_sales = []
# for line in lines:
#     line = line.split(",")
#     # 2904,4
#     total_sales, hours = line
#     avg = int(total_sales) / int(hours)
#     avg_sales.append(avg)
# print(avg_sales)

# Výjímky
# ZeroDivisionError	Деление на ноль (10 / 0)
# ValueError	Неверное преобразование типов (int("abc"))
# IndexError	Обращение к несуществующему индексу списка (my_list[10])
# KeyError	Обращение к несуществующему ключу в словаре (my_dict["neexistuje"])
# TypeError	Операция с несовместимыми типами ("abc" + 5, len(10))
# AttributeError	Обращение к несуществующему атрибуту (10.append(5))
# NameError	Использование неопределённой переменной (print(x), если x не объявлена)
# IndentationError	Ошибка отступов (if True:\nprint("Hello") без отступа)
# SyntaxError	Ошибка в синтаксисе (print "Hello" без скобок)
# FileNotFoundError	Файл не найден (open("neexistuje.txt"))

# ----------------------Cvičení: 1 Ošetření dělení nulou
# try:
#     a = float(input("Zadej první číslo: "))
#     b = float(input("Zadej druhé číslo: "))

#     vysledek = a / b
#     print(f"Výsledek dělení: {vysledek}")

# except ZeroDivisionError:
#     print("Chyba: dělení nulou není možné!")  # Обрабатываем ошибку деления на 0


# ----------------------Cvičení: 2 Čtení ze seznamu
# knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]

# try:
#     index = int(input("Zadej index knihy: ")) 
#     print(f"Vybraná kniha: {knihy[index]}")  
    
# except IndexError:
#     print("Chyba: Zadaný index není platný! Zadejte číslo mezi 0 a", len(knihy) - 1)
# except ValueError:
#     print("Chyba: Zadejte platné číslo!")  # Обрабатываем нечисловой ввод


# # ----------------------Bonus Cvičení: 3 Datum
# from datetime import datetime

# datum_narozeni = input("Zadej datum ve formátu RRRR-MM-DD: ")

# # 1. Ověření formátu (dvě pomlčky a části jsou čísla)
# casti = datum_narozeni.split("-")
# if len(casti) == 3 and all(c.isdigit() for c in casti):
#     try:
#         # 2. Ověření reálného data pomocí fromisoformat()
#         datum_narozeni = datetime.fromisoformat(datum_narozeni)
#         print(f"Zadané datum je platné: {datum_narozeni.date()}")
#     except ValueError:
#         print("Chyba: Zadané datum neexistuje!")
# else:
#     print("Chyba: Nesprávný formát data! Použij RRRR-MM-DD.")
