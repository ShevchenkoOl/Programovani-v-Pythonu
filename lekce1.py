#----------------------------------------------------------- Lekce 1 Úvod, slicing, metody, moduly
# Pro práci se seznamy se nám může hodit několik funkcí:

# len() : Vrátí délku seznamu

# sum() : Vrátí součet všech prvků v seznamu

# min() : Vrátí nejmenší prvek seznamu

# max() : Vrátí největší prvek seznamu

# sorted() : Vrátí setříděný seznam

# int() : převede pouze celé číslo, pokud překládám desítkové, vygeneruje se chyba  print(int("2")) // 2

# float() : převede číslo s plovoucí desetinnou čárkou print(float("2"))  // 2.0

# str() : převede číslo na řetězec



# venecky = [1, 2, 4, 1, 6, 0, 1]
# jmeno = 'martin' + ' ' + 'podloucký'

# venecky[5] = 12 # můžeme změnit hodnotu 5 (pátého) prvku seznamu
# print(venecky)  # [1, 2, 4, 1, 6, 12, 1]

# Můžeme také vytisknout část seznamu podél dané hranice
# print(venecky[2:5])    # [4, 1, 6]
# print(venecky[:3])     # [1, 2, 4]
# print(venecky[3:])     # [1, 6, 0, 1]
# print(jmeno[:4])       # mart
# print(jmeno[4:])       # in podloucký
# print(venecky[-1:])      # 1
# print(venecky[-5:])      # [4, 1, 6, 0, 1]
# print(jmeno[::-1])        # ýkcuoldop nitram
# # print(jmeno[:: 2])         # mri oluk
# print(sorted(venecky))  # [0, 1, 1, 1, 2, 4, 6]
# print(sorted(venecky, reverse=True)) # [6, 4, 2, 1, 1, 1, 0]

#---------------operátor in
# inzerat = "Na této pracovní pozici budete využívat Python a SQL"
# if "Python" in inzerat:
#     print("Je to pro mě!")
# else:
#     print("Je mi lito((")


#---------------operátor not in
# email = "spatny_mail.cz"
# if "@" not in email:
#     print("V e-mailu chybí zavináč!")
# else:
#     print("E-mail je v poradku")


#-----------------------------------Cvičení 1 Pohyby na účtu
# pohyby = [1200, -250, -800, 540, 721, -613, -222]
# print(pohyby[2])    # Vypište v pořadí třetí pohyb z uvedeného seznamu.
# print(pohyby[2:])   # Vypište všechny pohyby kromě prvních dvou.
# print(len(pohyby))  # Vypište kolik je všech pohybů dohromady.
# print(max(pohyby))  # Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
# print(min(pohyby))
# print(sum(pohyby))  # Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.



#-----------------------------------Cvičení 2 Průměr
# s = [1200, -250, -800, 540, 721, -613, -222]
# prumer = sum(s)/len(s)
# print(prumer)


#-----------------------------------Cvičení 3 Rozpětí
# s = [1200, -250, -800, 540, 721, -613, -222]
# rozpet = max(s) - min(s)
# print(rozpet)

# if min(s) < 0:
#    rozpet = max(s) + min(s)
# else:
#    rozpet = max(s) - min(s)
# print(rozpet)

#-----------------------------------Bonusy, Cvičení 4 Střed seznamu
# s = [1200, -250, -800, 540, 721, -613, -222, 47]
# if len(s) % 2 != 0:       # % zbytek po dělení 
#    print(s[len(s) // 2])  # index musí být celé číslo, proto použijeme celočíselné dělení //
# else:                     # python výsledkem normálního dělení je vždy hodnota s plovoucí desetinnou čárkou, proto používáme //
#    print(s[len(s) // 2 - 1], s[len(s) // 2]) 


#-----------------------------------Bonusy, Cvičení 5 Střed seznamu podruhé
# s = [1200, -250, -800, 540, 721, -613, -222, 47]
# if len(s) % 2 != 0:
#    print(s[len(s) // 2])  
# else:                     
#    print(s[len(s) // 2 - 1])




#-----------------------------------Řetězce, metody
# print('  martin   '.strip())            # martin
# print('3.12,4.1,9.6,-127,0'.split(',')) # ['3.12', '4.1', '9.6', '-127', '0']
# print('+'.join(['1', '2', '3', '4']))   # 1+2+3+4

# text = "Kurz vede lektor Marek"
# novy_text = text.replace("Marek", "Martin")
# print(novy_text)                        # Kurz vede lektor Martin
# seznam = ["a", "b", "a", "a"]
# seznam2 = ['car', 'flower', 'flower', 'home', 'PC']
# print(seznam.count("a")) # 3  
# print(seznam2.count("home")) # 1
# print('  martin   '.strip())   # martin
# print('po ut st čt pá'.split(' ')) # ['po', 'ut', 'st', 'čt', 'pá']
# print('/'.join(['dokumenty', 'dapraha', 'python', 'priklady'])) # dokumenty/dapraha/python/priklady



#-----------------------------------Řetězce, metody Cvičení 1 Převod písmen
# jmeno = "Oleksii"
# print(jmeno.lower())


#-----------------------------------Řetězce, metody Cvičení 2 Čísla jako text
# hodnoty = ['12', '1', '7', '-11']
# cislo = int(hodnoty[2]) + 4
# hodnoty[2] = str(cislo)
# print(hodnoty)     # ['12', '1', '11', '-11']


#-----------------------------------Řetězce, metody Cvičení 3 Čísla v textu
# hodnoty = '12.1 1.68 7.45 -11.51'
# seznam = hodnoty.split()
# seznam[3] = str(float(seznam[3]) + 0.25)
# nova_hodnota = ' '.join(seznam)
# print(nova_hodnota)      # 12.1 1.68 7.45 -11.26





#------------------------------------ Moduly
# import math
# print(math.ceil(3.1))  # 4
# print(math.floor(3.7))  # 3

# import statistics      # statistics.mean() - aritmetický průměr
# print(statistics.mean([1, 2, 3, 4, 5, 6]))  # 3.5
# print(statistics.mode(["red", "blue", "blue", "red", "green", "red", "red"])) # 'red'  # vrátí prvek seznamu, který se často vyskytuje


#-----------------------------------Moduly Cvičení 1 Zaokrouhlování
# import math
# print(math.ceil(3.1))  # 4
# print(math.floor(3.7))  # 3
# print(round(3.7))     # 4
# print(round(2.5))     # 2  funkce aroun() děla zaokrouhlování bankéře, to znamená, že pokud desetine číslo končí 0,5,
                        #    zaokrouhlí se na nejbližší sudé číslo, bez ohledu na to, zda je nahoru nebo dolů
# print(round(3.5))     # 4
# print(round(6.5))     # 6


#-----------------------------------Moduly Bonusy Cvičení 2  Přijímačky a moduly
# import statistics
# school_report = [
#     ["Český jazyk", 1],
#     ["Anglický jazyk", 1],
#     ["Matematika", 1],
#     ["Přírodopis", 2],
#     ["Dějepis", 1],
#     ["Fyzika", 2],
#     ["Hudební výchova", 4],
#     ["Výtvarná výchova", 2],
#     ["Tělesná výchova", 3],
#     ["Chemie", 4],
# ]
# dulozite = []

#----Variant 1 
# for predmet in school_report:
#     if predmet[0] == "Český jazyk" or predmet[0] == "Anglický jazyk" or predmet[0] == "Matematika" or predmet[0] == "Fyzika":
#        dulozite.append(predmet[1])

#-----Varian 2
# for predmet, znamka in school_report:    # python automaticky rozbalí náš seznam do dvou prvků
#     if predmet == "Český jazyk" or predmet == "Anglický jazyk" or predmet == "Matematika" or predmet == "Fyzika":
#        dulozite.append(znamka)


# prumer = statistics.mean(dulozite)
# print(prumer)        # 1.25
# print(max(dulozite)) # 2
# print(min(dulozite)) # 1



#-----------------------------------Moduly Bonusy Cvičení 3 Vánoční party
# import statistics
# votes = [
#     "curling", 
#     "vánoční svařák na trzích", 
#     "vánoční svařák na trzích", 
#     "curling", 
#     "zážitková první pomoc",
#     "curling", 
#     "zážitková první pomoc",
#     "curling",
#     "zážitková první pomoc",
#     ]
# print(statistics.mode(votes)) # curling