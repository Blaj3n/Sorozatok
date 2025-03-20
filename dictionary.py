konyvtar = {
    "auto": "BMW",
    "evjarat": 2005,
    "kombi": True,
    "szín": ["fekete", "fehér", "kék"]
}

print(konyvtar["kombi"])
print(konyvtar.keys()) # list []
print(konyvtar.values()) # list []
print(konyvtar.items()) # tupples ()
print(konyvtar)
konyvtar["hossz"] = 18
print(konyvtar)

nev = "xxxxxHelloxxx"
print(nev.strip())