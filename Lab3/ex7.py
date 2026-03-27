preturi = [100, 50, None, 200, None, 80, 120, 470, None]

preturi_valide = list(filter(lambda x: x is not None, preturi))
preturi_reduse = list(map(lambda x: x * 0.9, preturi_valide))

print("Preturi initiale:", preturi)
print("Preturi fara None:", preturi_valide)
print("Preturi reduse (10%):", preturi_reduse)