# ------------------------------------- Lekce 11 Regulární výrazy

# \d+\.\s?\d+\.\s?\d+
# 19. 12. 2020
# 19.12.2020


# \d{6,10}/\d{4}
# 123456-1234567890/0300
# 123456/0325
# 251-123456789/0550


# \d+\. \w+\. \d+ (sobota|neděle)
# 9. led. 2021 sobota 9:30 - 16:30 Úvod do programování 1 - Java
# 16. led. 2021 sobota 7:30 - 15:30 Úvod do programování 1 - JavaScript
# 16. led. 2021 sobota 8:30 - 17:30 Úvod do programování 2 - Python
# 18. led. 2021 úterý 9:30 - 17:30 Úvod do programování 1 - JavaScript
# 23. led. 2021 sobota 9:30 - 16:30 Úvod do programování 2 - Java
# 27. led. 2021 středa 9:30 - 17:30 Úvod do HTML a CSS
# 7. úno. 2021 neděle 8:30 - 17:30 Úvod do programování 1 - Python ONLINE
# 14. úno. 2021 neděle 8:30 - 17:30 Úvod do programování 1 - Python ONLINE
# 20. úno. 2021 sobota 9:30 - 17:30 Testuju Úvod do testování - manuální


# ----------------------------------Cvičení: 1 Předčíslí u čísla účtu
#  123456/7890 nebo 123456-7890/1234

# \d{1,6}-?\d{6,10}/\d{4}

# Vysvětlení:
# \d{1,6}: Předčíslí (1 až 6 číslic).
# -?: Volitelná pomlčka (0 nebo 1 výskyt).
# \d{6,10}: Číslo účtu (6 až 10 číslic).
# /: Lomítko oddělující číslo účtu a kód banky.
# \d{4}: Kód banky (4 číslice).


# ----------------------------------Cvičení: 2 Číslo účtu podruhé
# ^[12][012]\d{8}/2100$
# Vysvětlení:
# ^ — Začátek řetězce.
# [12] — První číslice může být pouze 1 nebo 2.
# [012] — Druhá číslice může být pouze 0, 1 nebo 2.
# \d{8} — Následuje 8 libovolných číslic (pro zbytek čísla účtu).
# o, odděluje číslo účtu od kódu banky.
# 2100 — Kód banky je vždy "2100".
# $ — Konec řetězce.

# 2200123456/2100
# 2100223344/2100
# 1100998877/2100


# ----------------------------------Cvičení: 3 Registrační značka
# Regulární výraz pro základní kontrolu:

# ^\d[A-Z0-9] \d{4}$

# Tento regulární výraz splňuje následující podmínky:
# Začíná číslicí (\d).
# Následuje písmeno nebo číslice ([A-Z0-9]).
# Po mezeře následuje čtveřice čísel (\d{4}).
# Konec řetězce je označen $, což znamená, že text musí být ukončen právě po čtyřech číslicích.
# Upravený regulární výraz pro konkrétní kraj (druhý znak je jeden z povolených krajů):
# ruby

# ^\d[ABCHEJKLMPSTUZ] \d{4}$
# V tomto případě:
# Druhé písmeno ([ABCHEJKLMPSTUZ]) bude omezeno na konkrétní kraje, tedy na jednu z hodnot: A, B, C, E, H, J, K, L, M, P, S, T, U, Z.
# Zbytek formátu zůstává stejný.


# ----------------------------------Cvičení: 4 Telefonní číslo
# Regulární výraz pro základní telefonní číslo (9 číslic):
# ^\d{9}$

# Regulární výraz pro telefonní číslo s mezerami mezi trojicemi:
# ^\d{3} \d{3} \d{3}$

# Regulární výraz pro telefonní číslo s mezinárodní předvolbou +420:
# ^\+420 \d{3} \d{3} \d{3}$

# Kombinovaný regulární výraz pro číslo s mezerami, bez mezer, s mezinárodní předvolbou nebo bez ní:
# (^\+420 ?\d{3} ?\d{3} ?\d{3}$|^\d{9}$)


# ----------------------------------Cvičení: 5 Ministerstva
# Ministerstvo [A-Za-zá-žÁ-Ž\s]+

# Vysvětlení:
# Ministerstvo — hledá slovo "Ministerstvo".
# [A-Za-zá-žÁ-Ž\s]+ — hledá jakýkoli text (písmena a mezery) za slovem "Ministerstvo". Tato část je opakována alespoň jednou, což znamená, že vybere celý název ministerstva.


# ----------------------------------Cvičení: 6 Slavný soude
# ^\d{1,2} [A-Z]{1,3} \d{1,4}/\d{4}$

# Vysvětlení:
# ^\d{1,2} — na začátku máme 1 až 2 číslice (číslo soudního oddělení).
# [A-Z]{1,3} — následuje 1 až 3 velká písmena (rejstříková značka).
# \d{1,4} — dále jsou 1 až 4 číslice (běžné číslo).
# / — lomítko.
# \d{4}$ — čtyřmístný ročník (4 číslice na konci).


# ----------------------------------Cvičení: 7 Ave, Caesar!
# [MDCLXVI]{1,4}\.

# Vysvětlení:
# [MDCLXVI]{1,4} — vybere 1 až 4 znaky, které mohou být M, D, C, L, X, V, I (písmena, která tvoří římské číslice).
# \. — tečka na konci, která se vyskytuje po římských číslicích (např. "IX." nebo "VII.").


# import re
# regularni_vyraz = re.compile(r"\d{9,10}")