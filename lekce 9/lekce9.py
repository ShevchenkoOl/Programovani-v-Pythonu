#-----------------------------------------------------Lekce 9 Formát JSON
# import json # modul

#-------------Čtení JSON dat
# with open("absolventi.json", encoding="utf-8") as file:
#     absolvents = json.load(file)
    
# print(absolvents[0]) # prvni absolvent


#-------------Zápis JSON dat
# hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
# with open("hodiny.json", mode="w", encoding="utf-8") as file:
#     json.dump(hours, file, indent=2)


#--------------Diakritika v JSON
# data = {"řeřicha": "Česká Třebová"}

# with open("rericha.json", mode="w", encoding="utf-8") as file:
#     json.dump(data, file, indent=4, ensure_ascii=False)
    

#--------------Stahování dat z internetu
# pip install requests

# import requests

# response = requests.get('https://api.kodim.cz/python-data/people')
# data = response.json()
# print(data)   

    
#--------------------------Cvičení: 1 Seznam lidí
# import requests

# response = requests.get('https://api.kodim.cz/python-data/people')
# data = response.json()

# # Zjistěte kolik lidí celkem seznam obsahuje:
# print(len(data))  # 1000

# # Zjistěte jaké všechny informace máme o jednotlivých osobách.
# print(data[0].keys()) # dict_keys(['first_name', 'last_name', 'email', 'gender'])
# print(list(data[0].keys())) # ['first_name', 'last_name', 'email', 'gender']

# # Zjistěte, kolik je v souboru mužů a žen.
# count_male = 0
# count_female = 0

# for person in data:
#     if person["gender"] == "Male":
#         count_male += 1
#     else:
#         count_female += 1
# print(f"v souboru jsou mužů: {count_male}, žen: {count_female}") # v souboru jsou mužů: 489, žen: 511


#--------------------------Cvičení: 2 Kočky
# import requests
# import json

# response = requests.get('https://catfact.ninja/fact')
# data = response.json()
# fact_data = {"fact": data["fact"]}

# with open("fact.json", mode="w", encoding="utf-8") as file:
#     json.dump(fact_data, file)


#--------------------------Bonus Cvičení 1: Svátky
# import requests

# # response = requests.get('https://svatky.adresa.info/json')
# # data = response.json()
# # print(f"Dneska svatek ma: {data[0]['name']}") # Dneska svatek ma: Emanuel


# date = int(input("Nastavte den ve formátu DDMM, abyste zjistili, kdo má v daný den svátek: "))
# response = requests.get(f'https://svatky.adresa.info/json?date={date}')
# data = response.json()
# if data:
#     print(f"{date} svatek ma: {data[0]['name']}") # 29. února svatek ma: Horymírl
# else:
#      print(f"Pro tento den ({date}) není žádný svátek.")


# import requests

# # Запрашиваем дату у пользователя
# date = input("Nastavte den ve formátu DDMM, abyste zjistili, kdo má v daný den svátek: ")
# url = 'https://svatky.adresa.info/json'
# params = {'date': date}

# # Отправляем GET запрос с параметрами
# response = requests.get(url, params=params)

# data = response.json()
# if data:  # Если список data не пустой
#     print(f"{date} svátek má: {data[0]['name']}")
# else:
#     print(f"Pro tento den ({date}) není žádný svátek.")



#--------------------------Bonus Cvičení 2: Jména
# import requests

# # Вводим имя
# name = input("Zadejte jméno pro odhad národnosti: ")

# # Делаем запрос к API
# response = requests.get(f'https://api.nationalize.io/?name={name}')

# # Преобразуем ответ в формат JSON
# data = response.json()

# # Находим страну с наибольшей вероятностью
# most_probable_country = max(data["country"], key=lambda x: x["probability"])

# # Выводим результат
# print(f"Nejvíce pravděpodobná národnost pro jméno '{name}' je: {most_probable_country['country_id']} "
#       f"se pravděpodobností {most_probable_country['probability']:.3f}")




#--------------------- Složitější JSON struktury
# import json
# with open('zavod.json', encoding='utf-8') as file:
#     runners = json.load(file)
# winner = runners[0]
# winner_time = winner["casy"]["oficialni"]
# print(winner, winner_time)


#--------------------------Cvičení 1: Závod
# import json
# with open('zavod.json', encoding='utf-8') as file:
#     runners = json.load(file)

# finishers = []
# for zavodnik in runners:
#     if zavodnik["casy"]["oficialni"] != "DNF":
#          finishers.append([zavodnik["jmeno"], zavodnik["casy"]["oficialni"]])
# print(finishers)
# print(finishers[1])


#--------------------------Cvičení 2: Transformace dat
# import json

# # Předpokládáme, že soubor words.txt je v aktuálním adresáři
# with open('words.txt', 'r', encoding='utf-8') as file:
#     words = file.read().splitlines()  # Přečteme soubor a rozdělíme na seznam slov

# # Vytvoříme prázdný slovník pro uložení slov podle písmen
# word_dict = {}

# # Projdeme všechna slova
# for word in words:
#     first_letter = word[0].upper()  # První písmeno slova, převedeno na velké písmeno
#     if first_letter not in word_dict:
#         word_dict[first_letter] = []  # Pokud písmeno ještě není v slovníku, vytvoříme seznam
#     word_dict[first_letter].append(word)  # Přidáme slovo do seznamu pro dané písmeno

# # Seřadíme seznamy slov v každém klíči abecedně
# for key in word_dict:
#     word_dict[key].sort()

# # Seřadíme samotné klíče slovníku abecedně
# sorted_word_dict = dict(sorted(word_dict.items()))

# # Uložíme výstup do souboru JSON
# with open('output.json', 'w', encoding='utf-8') as json_file:
#     json.dump(sorted_word_dict, json_file, ensure_ascii=False, indent=4)

# print("Výstupní soubor byl úspěšně vytvořen.")
