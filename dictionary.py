konyvtar = {
    "auto": "BMW",
    "evjarat": 2005,
    "kombi": True,
    "szín": ["fekete", "fehér", "kék"]
}

print(konyvtar["kombi"])
print(konyvtar.keys())      # list []
print(konyvtar.values())    # list []
print(konyvtar.items())     # tupples ()
print(konyvtar)
konyvtar["hossz"] = 18
print(konyvtar)

nev = "xxxxxHelloxxx"
print(nev.strip())
float = 8 / 6 # a századot pontosan mutatja
print(float)

div = 8 // 3 # div = egész osztás
print(div)

mod = 6 % 5 # maradékos osztás
print(mod)

lista = [1, 2, 3, 4, 5]
for egyelem in lista:
    if egyelem % 2 == 0:
        lista.remove(egyelem)
print(lista)

# int = 6
# string = "fg"
# float, bool, lista, set, dict, complex
lista = ["alma", "körte", "2"]  # abcdefgh...0123456789
print(max(lista))
lista = ["1", "2:7", "2:8", "1002345457687"]    # 0123456789
print(max(lista))


# def szamolo(a:int, b:int) -> int:
#     return a + b
# szam_1 = int(input("Kérek egy számot: "))
# szam_2 = int(input("Kérek egy számot: "))
# print(szamolo(szam_1, szam_2))
#
# def helo(nev:str):
#     print(f"Hello {nev} ")
#
# helo(str(szam_1))

a = set([2, 3, 4, 1, 5])    # settet hozunk létre
print(a)
print(type(a))

b = set(range(0, 11))
print(b)

konyvtar_1 = {
    "auto": "BMW",
    "evjarat": 2005,
    "kombi": True,
    "szín": ["fekete", "fehér", "kék"]
}

c = set(konyvtar_1)
print(c)

szoveg = "Szia Bence mi a helyzet?"
print(szoveg.split())   # vág(split()) a jel alapján, és LISTÁBA helyezi a tagokat.
s = konyvtar_1.get("szín", 0) # knyvtar.get("key feltétel", None helyett)
print(s)