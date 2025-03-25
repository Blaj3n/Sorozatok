konyvtar = {
    "auto": "BMW",
    "evjarat": 2005,
    "kombi": True,
    "szín": ["fekete", "fehér", "kék"]
}

# print(konyvtar["kombi"])
# print(konyvtar.keys())      # list []
# print(konyvtar.values())    # list []
# print(konyvtar.items())     # tupples ()
# print(konyvtar)
# konyvtar["hossz"] = 18
# print(konyvtar)
#
# nev = "xxxxxHelloxxx"
# print(nev.strip())
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