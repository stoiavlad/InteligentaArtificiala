print("Procesam tranzactiile...")

risc = ["Coreea de Nord", "Siria", "Iran"]
suspecte = 0

n = int(input("Cate tranzactii introduci? "))

for i in range(n):
    suma = int(input("Suma: "))
    tara = input("Tara: ")

    if suma > 10000:
        print("Tranzactie:", suma, "RON din", tara, "→ Suspicioasa (suma mare)")
        suspecte += 1

    elif tara in risc:
        print("Tranzactie:", suma, "RON din", tara, "→ Frauduloasa (tara cu risc)")
        suspecte += 1

    elif n > 3:
        print("Tranzactie:", suma, "RON din", tara, "→ Activitate suspecta (prea multe tranzactii)")
        suspecte += 1

    else:
        print("Tranzactie:", suma, "RON din", tara, "→ Sigura")

if suspecte >= 3:
    print("Cont blocat! Prea multe tranzactii suspecte.")
else:
    print("Cont in regula.")