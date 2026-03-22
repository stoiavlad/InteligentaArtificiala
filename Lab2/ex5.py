import random

print("Bine ai venit la Loteria !")
print("Alege 6 numere intre 1 si 49.")

alese = []

for i in range(6):
    nr = int(input("Numarul " + str(i+1) + ": "))
    alese.append(nr)

extrase = []

for i in range(6):
    extrase.append(random.randint(1, 49))

print("Numere extrase:", extrase)

potrivite = []

for nr in alese:
    if nr in extrase:
        potrivite.append(nr)

print("Ai ghicit", len(potrivite), "numere:", potrivite)

if len(potrivite) >= 3:
    print("Felicitari! Ai castigat un premiu mic!")
else:
    print("Mai incearca!")