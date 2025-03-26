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
# print(epizodok)

print("2. feladat")
darab = 0
for epizod in epizodok:
    if "NI" not in epizod["datum"]:
        darab += 1
print(f"A listában {darab} db vetítési dátummal rendelkező epizód van.\n")

# print("2. feladat 2.")
# vetitik = ["" for epizod in epizodok if "NI" not in epizod["datum"]]    # list compr.
# print(f"A listában {len(vetitik)} db vetítési dátummal rendelkező epizód van.")

print("3. feladat")
latta = 0
for epizod in epizodok:
    if epizod["latta"]:
        latta += 1
szazalek = latta / len(epizodok) * 100
print(f"A listában lévő epizódok {szazalek:.2f}%-át látta.\n")

print("4. feladat")
ido_perc = 0
for epizod in epizodok:
    if epizod["latta"]:
        ido_perc += epizod["hossz"]
# print(ido_perc)
nap = ido_perc // (24 * 60)     # Div
ora = ido_perc % (24 * 60) // 60
perc = ido_perc % 60
print(f"Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött.\n")

print("5. feladat")
bekert_datum = input("Adjon meg egy dátumot! Dátum= ")  # 2017.11.03 < 2017.11.04
for epizod in epizodok:
    if epizod["datum"] <= bekert_datum and not epizod["latta"]:
        print(f"{epizod["resz"]}\t {epizod["nev"]}")
print("")
# print("6. feladat")


def hetnapja(ev:int, ho:int, nap:int) -> str:
    napok = ['v', 'h', 'k', 'sze', 'cs', 'p', 'szo']
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev -= 1
    hetnapja = napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho - 1] + nap) % 7]
    return hetnapja
# print(hetnapja(2005, 9, 2))


print("7. feladat")
napocska = input("Adja meg a hét egy napját (például cs)! Nap= ")
aznapi_sorozatok = set()
for epizod in epizodok:
    if "NI" not in epizod["datum"]:
        splitelve = epizod["datum"].split(".")
        # napos = hetnapja(int(epizod["datum"][:4]), int(epizod["datum"][5:7]), int(epizod["datum"][8:]))
        napos = hetnapja(int(splitelve[0]), int(splitelve[1]), int(splitelve[2]))
    if napos == napocska:
        aznapi_sorozatok.add(epizod["nev"])
if len(aznapi_sorozatok):
    for egyelem in aznapi_sorozatok:
        print(egyelem)
else:
    print("Az adott napon nem kerül adásba sorozat.")

print("")

print("8. feladat")

# sorozatok_konyvtar = {"Cím": {"hany_resz": 7, "hossza_ossz": 420}}
sorozatok_konyvtar = {}
for epizod in epizodok:
    if sorozatok_konyvtar.get(epizod["nev"], 0):
        sorozatok_konyvtar[epizod["nev"]]["hany_resz"] += 1
        sorozatok_konyvtar[epizod["nev"]]["hossza_ossz"] += epizod["hossz"]
    else: # not in
        # ez a behelyezése a konyvtárba, azaz még nem tettük bele.
        sorozatok_konyvtar[epizod["nev"]] = {}
        sorozatok_konyvtar[epizod["nev"]]["hossza_ossz"] = epizod["hossz"]
        sorozatok_konyvtar[epizod["nev"]]["hany_resz"] = 1
# with open("summa.txt", "w", encoding="utf-8") as f:
#     for egyelem in sorozatok_konyvtar:
#         print(egyelem, sorozatok_konyvtar[egyelem]["hossz_ossz"], sorozatok_konyvtar[egyelem]["resz"], file = f)