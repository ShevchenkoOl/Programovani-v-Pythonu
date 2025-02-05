#------------------------Lekce 2 Vlastní funkce
# def greet_user():  # def - definici funkce, nazev_funkce(parametry)
#     print("Ahoj!") # tělo funkce 

# greet_user()       # volani funkce
#                    # po vyvolání funkce se spustí print()  a zobrazí se konzole 'Ahoj'
# def sum_two_numbers(a, b):
#     return a + b

# suma_cisel = sum_two_numbers(3, 5)
# print(suma_cisel)   # 8


#------------------------- Cvičení 1, Násobení
# def multi(a, b):
#     return(a * b)
# print(multi(5, 3))  # 15



#------------------------- Cvičení 2, Funkce pro převody jednotek
# def kilometry_na_mile(kilometry): 
#     return (kilometry * 0.621371)
# print(kilometry_na_mile(5)) # 310686

# def mily_na_kilometry(mile):
#     return (mile * 1.60934)
# print(mily_na_kilometry(5)) # 8.0467

# # umožňují převod mezi metry a stopami:
# def metry_na_stopy(metry):
#     return(metry * 3.28084)
# print(metry_na_stopy(3))  # 9.84252
    
# def stopy_na_metry(stopy):
#     return(stopy * 0.3048)
# print(stopy_na_metry(3))  # 0.9144

# # které umožní převod mezi centimetry a palci:
# def centimetry_na_palec(centimetry):
#     return(centimetry * 0.393701)
# print(centimetry_na_palec(3))  # 1.181103

# def palce_na_centimetry(palce):
#     return(palce * 2.54)
# print(palce_na_centimetry(3))  # 7.62

# # které provedou převod mezi kilogramy a librami.
# def kilogramy_na_libry(kilogramy):
#     return(kilogramy * 2.20462) 
# print(kilogramy_na_libry(3))  # 6.613859

# def libry_na_kilogramy(libry):
#     return(libry * 0.453592)
# print(libry_na_kilogramy(5))  # 2.26796

# # které umožní převod mezi litry a galony:
# def litry_na_galony(litry):
#     return(litry * 0.3)
# print(litry_na_galony(3)) # 0.8999

# def galony_na_litry(galony):
#     return(galony * 3.8)
# print(galony_na_litry(3)) # 11.399999

# # které umožní převod rychlosti mezi kilometry za hodinu a míli za hodinu:
# def kmh_na_mph(kmh):
#     return(kmh * 0.621371)
# print(kmh_na_mph(50))  # 31.0686

# def mph_na_kmh(mph):
#     return(mph * 1.60934)
# print(mph_na_kmh(20))  #32.1868

# # které umožňují převod teploty mezi stupni Celsia a stupni Fahrenheit:
# def celsia_na_fahrenheit(teplota):
#     return((teplota * 9 / 5)+32)
# print(celsia_na_fahrenheit(20))  # 68.0

# def fahrenheit_na_celsia(teplota):
#     return((teplota - 32) * 5 / 9)
# print(fahrenheit_na_celsia(20))  # -6.6666666


#-------------------------Bonusy Cvičení 3 Měsíc narození
# def month_of_birth(rodne_cislo):
#     if str(rodne_cislo)[2] in ("0", "5"):  # zkontrolujeme, zda je druhá pozice 0 nebo 5
#         return str(rodne_cislo)[3] 
#     else:
#         return ("1" + str(rodne_cislo)[3]) 

# print(month_of_birth(8561201439))  # Výstup: 11


#-------------------------Bonusy Cvičení 4 Rámeček
# word = input("Zadei slovo ")
# def obal(slovo):
#     length = len(slovo) + 4
#     # print("*" * length)
#     # print(f'* {slovo} *')
#     # print("*" * length)
#     print(f' {"*" * length}\n * {slovo} *\n {"*" * length}')
# obal(word)



# #-------------------------Bonusová cvičení 1 Hotel
# def total_price(person, breakfast=False):
#     if breakfast:
#         return(person * 975)
#     else:
#         return(person * 850)
# print(total_price(1))



#-------------------------Bonusová cvičení 2 Ruleta
# import random
# rad1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
# rad2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
# rad3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
# print("Máme tři řady čísel: \n - první řada (hodnoty 1, 4, 7 atd.);\n - druhá řada (hodnoty 2, 5, 8 atd.);\n - třetí řada (hodnoty 3, 6, 9 atd.).")
# rada = int(input("Zadejte prosím číslo řádku od 1 do 3, na který chcete vsadit: "))
# sazka = float(input("Uveďte prosím částku sázky, kterou chcete vložit: "))
# def roulette(cislo_rady, sazka):
#     vypadlo = random.randint(0, 36)
#     print(f'Vypadlo cislo: {vypadlo}')

# # pokud padne 0, uživatel vždy prohrává.
#     if vypadlo == 0:
#         print('Bohužel výpadlo 0, nikdo nevyhrál!')
#         return
# # nebo kdyz vydere 0:
#     if vypadlo == 0 and cislo_rady == 0:
#         print(f'Jupiiii, jste vyhral {sazka * 5} cze)))))')
#         return

#     if   vypadlo in rad1:
#          vyhral_rad = 1
#     elif vypadlo in rad2:
#          vyhral_rad = 1
#     elif vypadlo in rad2:
#          vyhral_rad = 3
#     else: 
#          vyhral_rad = None

#     if cislo_rady == vyhral_rad:
#        print(f'Jupiiii, jste vyhral {sazka * 2} cze)))))')
#     else:
#         print('Bohužel jste prohráli, zkuste štěstí později((((')
# roulette(rada, sazka)


#-------------------------Bonusová cvičení 3 Zarovnání výpisu
# numbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
# max = len(str(max(numbers)))   # Zjiskame kolik znaků zabírá nejdelší číslo ze seznamu
# def zarovani(number: str, znak: str = ' '): # druhý parametr, pokud jej neuvedeme, bude mezera
#     for number in numbers:
#         print(str(number).rjust(max, znak))
# zarovani(numbers)       # výsledek bude s mezerou
# zarovani(numbers, '*')  # výsledek bude s *



#-------------------------Bonusová cvičení 4 Zpřeházená písmena
# import random
# slovo = "shevchenko"
# def zmatena_pismena(slovo):
#     if len(slovo) <= 3:
#        print(slovo)
#     else:
#         cast_slovo = list(slovo[1:-1])
#         random.shuffle(cast_slovo)
#         zmatene_slovo = slovo[0] + ''.join(cast_slovo) + slovo[-1]
#         print(zmatene_slovo)
# zmatena_pismena(slovo)   # sevnhkhceo

#----Pro celu vetu:
# import random
# veta = "Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena. Stačí, když první a poslední písmeno je na své pozici zachováno. Napiš funkci, která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny znaky kromě prvního a posledního"
# def zmatena_pismena(veta):
#     nova_veta = []
#     for slovo in veta.split(' '):
#         if len(slovo) >= 3:
#            cast_slovo = list(slovo[1:-1])
#            random.shuffle(cast_slovo)
#            zmatene_slovo = slovo[0] + ''.join(cast_slovo) + slovo[-1]
#            nova_veta.append(zmatene_slovo)
#     print(" ".join(nova_veta))
# zmatena_pismena(veta)



#-------------------------Bonusová cvičení 5 Nápravy
# def spocitej_pokutu(pocet_naprav , hmotnost):
#     if pocet_naprav == 2:
#        pokuta = 18 - hmotnost
#     elif pocet_naprav == 3:
#         pokuta = 25 - hmotnost
#     elif pocet_naprav == 4:
#         pokuta = 32 - hmotnost
#     elif pocet_naprav == 5:
#         pokuta = 48 - hmotnost
#     else: 
#         return None
    
#     if pokuta >= 0:
#           print("Gratuluji, vase hmotnost je povolena")
#     else:
#           pokuta = pokuta * (-1000)
#           print(pokuta)

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
