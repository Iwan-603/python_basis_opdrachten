# Opdracht 1 lists
# Naam student:
# Groep:
mylist = []
dict_1 = { "id": 0, "voornaam": "jan", "achternaam": "varken" }
dict_2 = { "id": 1, "voornaam": "simon", "achternaam": "jtrkq" }
dict_3 = { "id": 2, "voornaam": "patrick", "achternaam": "wkjff" }
dict_4 = { "id": 3, "voornaam": "rick", "achternaam": "diktrom" }

mylist = []
for d in [dict_1, dict_2, dict_3, dict_4]:
    mylist.append(d)

print(mylist[1]["voornaam"], mylist[1]["achternaam"])