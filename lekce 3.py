#------------------------Lekce 3 Slovníky
# N-tice (tuple) v Pythonu jsou neměnné sekvence, které mohou obsahovat prvky různých typů:
example = "Oleksii", 25, True
print(example)        # ('Oleksii', 25, True)
print(type(example))  # <class 'tuple'>

name, age, isOnline = example
print(name)  # Oleksii

# Nezaměňovat se seznamem, seznam je vždy v hranatých závorkách []:
list = ["Oleksii", 25, True]
print(list)        # ['Oleksii', 25, True]
print(type(list))  # <class 'list'>



# Množiny (set)
names = set()
names.add("Oleklsii")
names.add('Denis')
print(names)             # {'Oleklsii', 'Denis'}
print(type(names))       # <class 'set'>
print(len(names), names) # 2 {'Denis', 'Oleklsii'}
names.add('Mariana')     
print(len(names), names) # 3 {'Denis', 'Oleklsii', 'Mariana'}
names.add(5)
print(names)             # {'Denis', 'Oleklsii', 'Mariana', 5}

# Vzájemné převádění datových typů
t = 1, 2, 3, 2, 3, 2, 3, 1, 2
s = set(t)
print(s)     # {1, 2, 3}


#----------------------------- Cvičení 1 Množiny                                             # Použití trojitých uvozovek ''' nebo """ se používá k přenosu velkých textů při zachování jejich struktury
text = """Prágl, po anglánsku Prague nebo Praha nebo v Cajsku, je taková lochna              # pokud použijeme print(text), text bude vytištěn přesně v zadaném formátu, se zachováním odstavců a pomlček
v tem kuse hródy někde za čárama naši domoviny, kde se zoncna už
nechláme a kde se prndá po cajzlovsku. A ještě k temu tam majó sicnu
těžcí papaláši, kvůli čemu ho má každé v láfu jako kaktus ve véfuku.
Z Práglu bere kramále aj ten jejich len kerému se péruje Vltava. O Práglu se taky kóří, pač tam majó hafo retychů pro všecky. Kromě
bůry švédských retychů só aj dva v Olmecu a jeden v Bučovicách.
To my z našeho štatlu radši hážem lulec do kašny na Zelňáku. Když
ale nekdo vopruboval zašrajbčit náš barocké Parnas do cancu retychů
pro všecky, přišmrdolili se ti Švédi s tým, že só proti a hókajó po
celé hródě, že ta vasra v tem se dá chlemtat.
"""

novySet = set(text)
print(len(novySet), novySet)     # 49 {'b', 'ý', 'Š', 'l', 'š', 'á', 'T', '\n', 'ž', 'A', 'o', ',', 'k', 't', 'ó', 'P', 'g', 'r', 'p', 'z', 'Z', 'O', 'd', 'a', 's', 'n', 'u', 'K', 'ň', 'v', 'V', 'e', 'ě', 'j', 'm', 'č', 'B', 'é', 'ř', '.', 'ů', 'c', 'i', 'h', 'y', 'C', ' ', 'í', 'f'}




#----------------------------- Cvičení 2 Vysvědčení
vysvedceni = {
    "český jazyk": 1,
    "Matematika": 1,
    "Informatika": 1
}
print(vysvedceni)                   # {'český jazyk': 1, 'Matematika': 1, 'Informatika': 1}

for predmet in vysvedceni:
    print(predmet, vysvedceni[predmet])     # český jazyk 1
                                             # Matematika 1
                                             # Informatika 1
#    nebo 
# metod items() - převede slovník na n-tici, 
print(vysvedceni.items())                   # dict_items([('český jazyk', 1), ('Matematika', 1), ('Informatika', 1)])

for predmet, znamka in vysvedceni.items():   # případy jsou potřebné pro pohodlnou iteraci klíčů a hodnot současně
    print(predmet, znamka)                   # český jazyk 1
                                             # Matematika 1
                                             # Informatika 1



#----------------------------- Cvičení 3 Detektivky
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

# Přidej do slovníku nově vydanou detektivku "Noc, která mě zabila", která zatím nebyla uvedena na trh, je tedy prodáno 0 kusů.
sales["Noc, která mě zabila"] = 0
print(sales)  # {'Zkus mě chytit': 4165, 'Vrah zavolá v deset': 5681, 'Zločinný steh': 2565, 'Noc, která mě zabila': 0}


# U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100.
sales["Vrah zavolá v deset"] += 100
print(sales)    # {'Zkus mě chytit': 4165, 'Vrah zavolá v deset': 5781, 'Zločinný steh': 2565, 'Noc, která mě zabila': 0}

# pokud chceme vypsat pouze druhý prvek slovníku:
print(list(sales.items())[1])  # ('Vrah zavolá v deset', 5781)

# pokud chceme vypsat pouze hodnotu druhého prvku slovníku:
print(list(sales.values())[1])  # 5781



#----------------------------- Cvičení 4 Tombola
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

cisloListku = int(input("Zadejte číslo listu: "))

if cisloListku in tombola:
   print(f'Vyhral: {tombola[cisloListku]}')
else:
   print("Bohužel nevyhráváš nic.")


#----------------------------- Bonusy. Cvičení 5 Paranoidní večírek.
passwords = {
    "Jiří": "tajne-heslo",
    "Natálie": "jeste-tajnejsi-heslo",
    "Klára": "nejtajnejsi-heslo"
}

host = input("Zadejte svoe jmeno: ")

if host in passwords:
    heslo = input("Zadejte svoe heslo: ")
    if heslo == passwords[host]:
       print( "Smíš vstoupit.")
    else:
        print("Vase heslo neni spravne")
else:
    print("Nejste na seznamu")
