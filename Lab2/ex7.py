comentariu = input("Introdu un comentariu: ")

pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
negative = ["urat", "prost", "groaznic", "dezamagitor"]

ok_poz = False
ok_neg = False

for cuv in pozitive:
    if cuv in comentariu:
        ok_poz = True

for cuv in negative:
    if cuv in comentariu:
        ok_neg = True

if ok_poz:
    print("Comentariu pozitiv!")
elif ok_neg:
    print("Comentariu negativ!")
else:
    print("Comentariu neutru.")