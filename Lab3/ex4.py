my_list = [6, 12, 19]

patrat = lambda lista: list(map(lambda x: x**2, lista))

rezultat = patrat(my_list)
print(rezultat)