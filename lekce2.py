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
#     return str(rodne_cislo)[3]
# print(month_of_birth(8507201439)) # 7


#-------------------------Bonusy Cvičení 4 Rámeček
# word = input("Zadei slovo ")
# def obal(slovo):
#     length = len(slovo) + 4
#     print("*" * length)
#     print(f'* {slovo} *')
#     print("*" * length)
# obal(word)

