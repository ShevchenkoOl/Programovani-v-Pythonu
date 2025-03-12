#-----------------------------------------Datum a čas
# import datetime
# print(datetime.datetime.now()) # 2025-03-12 18:10:01.184651

from datetime import datetime, timedelta
# print(datetime.now) # 2025-03-12 18:10:01.184651

# apollo_start = datetime(1969, 7, 16, 14, 32)
# print(apollo_start) # 1969-07-16 14:32:00
# print(apollo_start.isoweekday()) # 3 day of week
# print(apollo_start.month) # 7
# print(apollo_start.strftime("%d. %m. %Y, %H:%M")) # 16. 07. 1969, 14:32

# apollo_pristani = datetime.fromisoformat("1969-07-21T18:54:00")
# print(apollo_pristani) # 1969-07-21 18:54:00

# apollo_pristani = datetime.strptime("21. 7. 1969, 18:54", "%d. %m. %Y, %H:%M")
# print(apollo_pristani) # 1969-07-21 18:54:00

# delka_mise = apollo_pristani - apollo_start
# print(delka_mise) # 5 days, 4:22:00

# -----------------------------Cvičení: 1 Převod času
# from datetime import datetime, timedelta
# apollo_start = datetime(1969, 7, 16, 14, 32)
# print(apollo_start.strftime("%m/%d/%Y")) # 07/16/1969

# -----------------------------Cvičení: 2 Čas od startu
# from datetime import datetime, timedelta
# days_in_week = {
#     0: "Monday",
#     1: "Tuesday",
#     2: "Wednesday",
#     3: "Thursday",
#     4: "Friday",
#     5: "Saturday",
#     6: "Sunday"
# }

# so_start = datetime(2020, 2, 10, 5, 3)
# # Který den v týdnu Solar Orbiter odstartoval
# print(so_start.weekday()) # 0
# print(days_in_week[so_start.weekday()]) # Monday

# # Spočítej, kolik času od jeho startu uplynulo
# rozdil = datetime.now() - satelit_start
# print(f'{rozdil.days} dní od jeho startu uplynulo') # 1857 dní od jeho startu uplynulo

#----------------------------------Balíčky z internetu
# from faker import Faker
# fake = Faker()

# for _ in range(10):
#     print(fake.name())
#     print(fake.address())


#------------------------------Cvičení: 1 Česká jména
# from faker import Faker

# fake = Faker('cs_CZ') # Nastavení české lokalizace
# print("Ženské jméno:", fake.first_name_female()) # Generování ženských jmen
# print("Adressa: ", fake.address()) # Generování adres


#------------------------------Bonusy Cvičení: 2 Polidštění
# import humanize
# import locale

# # Large number
# large_number = 1000000000
# print(humanize.intword(large_number))  # Outputs '1 billion' or '1 milliard' depending on your locale

# # Small number
# small_number = 42
# print(humanize.apnumber(small_number))  # Outputs '42' in a more human-friendly format

# import locale

# # Set the locale to French
# locale.setlocale(locale.LC_ALL, 'uk_UA')
# print(humanize.intword(1000000000))  # This will output in French
