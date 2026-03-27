numere_pare = [x for x in range(0, 101) if x % 2 == 0]
cuburi_10 = [x**3 for x in range(1, 11)]

lista1 = [11, 2, 3, 4, 5, 9, 45]
lista2 = [3, 4, 5, 11, 6, 45, 7]
elemente_comune = [x for x in lista1 if x in lista2]

print("Numere pare 0-100:", numere_pare)
print("Cuburile primelor 10 numere:", cuburi_10)
print("Elemente comune:", elemente_comune)