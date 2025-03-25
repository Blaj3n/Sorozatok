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
            egy_epizod["hossz"] = int(adatok[3])
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

print("4. feladat")
ido_perc = 0
for epizod in epizodok:
    if epizod["latta"]:
        ido_perc += epizod["hossz"]
print(ido_perc)
nap = ido_perc // (24 * 60)     # Div
ora = ido_perc % (24 * 60) // 60
perc = ido_perc % 60
print(f"Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött.")

print("5. feladat")
bekert_datum = input("Adjon meg egy dátumot! Dátum= ")  # 2017.11.03 < 2017.11.04
for epizod in epizodok:
    if epizod["datum"] <= bekert_datum and not epizod["latta"]:
        print(f"{epizod["resz"]}\t {epizod["nev"]}")

print("6. feladat")


def hetnapja(ev:int, ho:int, nap:int) -> str:
    napok = ['v', 'h', 'k', 'sze', 'cs', 'p', 'szo']
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev -= 1
    hetnapja = napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho - 1] + nap) % 7]
    return hetnapja
print(hetnapja(2005, 9, 2))