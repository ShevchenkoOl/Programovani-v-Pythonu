# --------------------------------------------------------------------Co všechno už umíme, opakování:

# 1 Zvýšení hodnoty proměnné:
# cislo = 100
# cislo = 101
# print(cislo) #101

# # varianta 2
# cislo = 100
# print(cislo + 1) #101


# 2 Zvýšení hodnoty načtené ze vstupu od uživatele:
# cislo = int(input("Zadejte libovolné číslo "))
# print(cislo)
# print(cislo + 1)


# 3 Fahrnheit vs. Celsius
# fahrenheit = int(input("Zadejte počet stupňů ve Fahrenheita "))
# celsius = (5 * (fahrenheit - 32))/9
# print(f'{celsius} stupně Fahrenheita se budou rovnat {fahrenheit} stupním Celsia')

# celsius = int(input("Zadejte počet stupňů ve Celsius "))
# fahrenheit = (celsius * 9) / 5 + 32
# print(f'{fahrenheit} stupně Fahrenheita se budou rovnat {celsius} stupním Celsia')


# Příklady na procvičení

# 1 Součet čísel v seznamu:
# print(2 + 5)
# print(sum([2, 5]))  # pomocí funkce sum()


# 2 Největší prvek v seznamu
# seznam = [2, 8, 1, 15, 4]
# print(max(seznam))


# 3 Sudá čísla
# seznam = [2, 5, 3, 7, 8, 10, 14]
# for index in seznam:
#     if index % 2 == 0:
#        print(index)


# 4 Rozdělení čísel
# seznam = [2, 5, 3, 7, 8, 10, 14]
# sude = []
# liche = []
# for index in seznam:
#      if index % 2 == 0:
#         sude.append(index)
#      else:
#          liche.append(index)
# print(f'Seznam sudých čísel: {sude}')
# print(f'Seznam lichých čísel: {liche}')


# 5 Odstranění duplikátů
# seznam = [2, 5, 8, 7, 8, 10, 14, 5, 7, 25, 2]
# bezDublikatu = []
# for index in seznam:
#      if index not in bezDublikatu:
#         bezDublikatu.append(index)
# print(f'Seznam bez dublikatu čísel: {bezDublikatu}')


# 6 Bonusy, Přijímačky
# school_report = [
#     ["Český jazyk", 3],
#     ["Anglický jazyk", 2],
#     ["Matematika", 3],
#     ["Přírodopis", 2],
#     ["Dějepis", 1],
#     ["Fyzika", 2],
#     ["Hudební výchova", 4],
#     ["Výtvarná výchova", 2],
#     ["Tělesná výchova", 3],
#     ["Chemie", 4],
# ]
# sum_of_mark = 0

# for mark in school_report:
#     if mark[0] == "Český jazyk" or mark[0] == "Anglický jazyk" or mark[0] == "Matematika" or mark[0] == "Fyzika":
#         sum_of_mark += mark[1]
#     prumer = sum_of_mark / 4
# print(f'Průměr z jazyků, matematiky a fyziky je: {prumer}')


# 7 Bonusy, Rodná čísla
# rodna_cisla = [
#     "845128/6219",
#     "801002/5021",
#     "900116/8291",
#     "790501/7894",
#     "850706/9259",
#     "891222/1824",
#     "870327/9582",
#     "810602/6883",
#     "850512/5070",
#     "790531/7081"
# ]
# muz = []
# zena = []
# for clovek in rodna_cisla:
#     if clovek[2] == '5':
#         zena.append(clovek)
#     else:
#         muz.append(clovek)
# print(f'Dnes přišlo k lékaři {len(muz)} mužů')
# print(f'Dnes přišlo k lékaři {len(zena)} žen')