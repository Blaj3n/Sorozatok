# print("1. feladat")
# dictionary key:value
egy_epizod = {} # egy epizód adatait mutatja
epizodok = [] # az összes epizód

adatok = []
with open("lista.txt", "r", encoding="utf-8") as file:
    for egysor in file:
        adatok.append(egysor.strip())
        if len(adatok) == 5:
            egy_epizod["datum"] = adatok[0]
            egy_epizod["nev"] = adatok[1]
            egy_epizod["resz"] = adatok[2]
            egy_epizod["hossz"] = adatok[3]
            if adatok[4] == "1":
                egy_epizod["latta"] = True
            else:
                egy_epizod["latta"] = False

            epizodok.append(egy_epizod)
            egy_epizod = {}
            adatok = []
print(epizodok)

print("2. feladat 1.")
darab = 0
for epizod in epizodok:
    if "NI" not in epizod["datum"]:
        darab += 1
print(f"A listában {darab} db vetítési dátummal rendelkező epizód van.")

print("2. feladat 2.")
vetitik = ["" for epizod in epizodok if "NI" not in epizod["datum"]]    # list compr.
print(f"A listában {len(vetitik)} db vetítési dátummal rendelkező epizód van.")

print("3. feladat")
latta = 0
for epizod in epizodok:
    if epizod["latta"]:
        latta += 1
szazalek = latta / len(epizodok) * 100
print(f"A listában lévő epizódok {szazalek:.2f}%-át látta.")