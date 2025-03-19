#-------------------------------Lekce 8 Soubory: čtení a zápis
# with open("mereni.txt", encoding="utf-8") as file:
#     text = file.read()
# print(text)  # po      17.3
               # út      16.8
               # st      15.1
               # čt      13.2
               # pá      14.0
               # so      13.9
               # ne      15.8

# lines = []
# with open("mereni.txt", encoding="utf-8") as file:
#     for line in file:
#         # 'po\t17.3\n'
#         # ["po", "17.3"]
#         line_list = line.split("\t")
#         line_list[1] = float(line_list[1])
#         lines.append(line_list)
# print(lines)  # [['po', 17.3], ['út', 16.8], ['st', 15.1], ['čt', 13.2], ['pá', 14.0], ['so', 13.9], ['ne', 15.8]]


# temperatures = []
# with open("mereni.txt", encoding="utf-8") as file:
#     for line in file:
#         day, temperature = line.split("\t")
#         temperature = float(temperature)
#         temperatures.append(temperature)
# print(temperatures) # [17.3, 16.8, 15.1, 13.2, 14.0, 13.9, 15.8]


#------------------------------------------Cvičení: Čtení ze souborů
#--------------------------------------------------- 1 Výplata přesněji
# vykaz = []
# with open("vykaz.txt", encoding="utf-8") as file:
#     for line in file:
#         vykaz.append(int(line.strip()))  # Убираем пробелы/переводы строк и преобразуем в число

# print("Seznam hodin za každý měsíc:", vykaz)

# hourly_wage = float(input("Zadejte hodinovou mzdu: "))

# total_salary = sum(vykaz) * hourly_wage
# average_salary = total_salary / len(vykaz)

# print(f"Celková výplata za rok: {total_salary:.2f} Kč")
# print(f"Průměrná výplata na měsíc: {average_salary:.2f} Kč")


#-------------------------------------------------------- 2 Počet slov
# word_counts = []  # Список для хранения количества слов в каждой строке

# with open("praha.txt", encoding="utf-8") as file:
#     lines = file.readlines()  # Читаем все строки файла

# # Обрабатываем строки
# for line in lines:
#     words = line.strip().split()  # Разбиваем строку на слова по пробелам
#     word_counts.append(len(words))  # Запоминаем количество слов в строке

# # Выводим количество слов в каждой строке
# for i, count in enumerate(word_counts, start=1):
#     print(f"Řádek {i}: {count} slov")

# # Вычисляем общее количество слов
# total_words = sum(word_counts)
# print(f"Celkový počet slov v textu: {total_words}")

# # Проверяем, соответствует ли текст требованиям
# if total_words >= 150:
#     print("Zadání bylo splněno! ✅")
# else:
#     print("Text nemá dostatek slov. ❌")


#---------------------------------------------Bonus Půjčovna
# Инициализируем переменную для суммы
# total_km = 0

# # Открываем файл и читаем данные
# with open("auta.txt", encoding="utf-8") as file:
#     for line in file:
#         parts = line.strip().split()  # Разделяем строку по пробелу
#         if len(parts) == 2:  # Проверяем, что строка содержит два элемента (SPZ и пробег)
#             _, km_str = parts  # Второй элемент - пробег
#             km_str = km_str.replace(",", ".")  # Заменяем запятые на точки
#             total_km += float(km_str)  # Преобразуем в число и суммируем

# # Выводим результат
# print(f"Celkem ujetých kilometrů: {total_km * 1000:.0f} km")  # Умножаем на 1000


#------------------------------------------------Zápis do souboru

# names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']
# with open("text.txt", "w", encoding="utf-8") as file:
#     for item in names:
#         print(item, file=file)



#--------------------------------------------Cvičení: Zápis do souborů
#----------------------------------------------------1 Dny v měsíci
# pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# with open("kalendar.txt", "w", encoding="utf-8") as file:
#     for item in pocty_dni:
#         print(item, file=file)



#-------------------------------------------------2 Vytvoření souboru
# nazev_souboru = input("Zadejte název souboru: ")
# text = input("Zadejte text, který chcete zapsat do souboru: ")

# # Открываем файл в режиме записи ("w" - перезаписывает файл, если он уже существует)
# with open(nazev_souboru + ".txt", "w", encoding="utf-8") as file:
#     file.write(text + "\n")  # Добавляем перевод строки для удобства

# print(f"Text byl úspěšně zapsán do souboru {nazev_souboru}.")



#------------------------------------------------3 Rozepsaná výplata
# Читаем данные из файла
# mzda = []
# with open("lekce_08/vykaz.txt", encoding="utf-8") as file:
#     for line in file:
#         mzda.append(int(line.strip()))  # Преобразуем строки в числа

# # Вывод списка отработанных часов
# print("Počet odpracovaných hodin v jednotlivých měsících:", mzda)

# # Получаем почасовую ставку
# hodinova_mzda = float(input("Zadej hodinovou mzdu: "))

# # Открываем файл для записи результатов
# with open("vyplaty.txt", "w", encoding="utf-8") as output_file:
#     # Обрабатываем зарплату по месяцам
#     for i, hodiny in enumerate(mzda, start=1):
#         vyplata = hodiny * hodinova_mzda
#         # Выводим в терминал
#         print(f"Měsíc {i}: {vyplata:.2f} Kč")
#         # Записываем в файл
#         output_file.write(f"Měsíc {i}: {vyplata:.2f} Kč\n")

# print("Výplaty byly zapsány do souboru 'vyplaty.txt'.")
