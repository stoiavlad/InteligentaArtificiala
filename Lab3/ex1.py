def determina_castigator(alegere1, alegere2):
    if alegere1 == alegere2:
        return "Este egalitate!"
    elif (alegere1 == "piatra" and alegere2 == "foarfeca") or \
            (alegere1 == "foarfeca" and alegere2 == "hartie") or \
            (alegere1 == "hartie" and alegere2 == "piatra"):
        return "Felicitări Jucător 1! Ai câștigat!"
    else:
        return "Felicitări Jucător 2! Ai câștigat!"


def ruleaza_joc():
    optiuni_valide = ["piatra", "foarfeca", "hartie"]

    while True:
        print("\nRock-Paper-Scissors ")
        jucator1 = input("Jucator 1: ").strip().lower()
        jucator2 = input("Jucator 2: ").strip().lower()

        if jucator1 not in optiuni_valide or jucator2 not in optiuni_valide:
            print("Alegere invalidă! Vă rugăm să alegeți doar dintre Piatra, Foarfeca sau Hartie.")
            continue

        rezultat = determina_castigator(jucator1, jucator2)
        print(rezultat)

        nou_joc = input("\nDoriți să începeți un nou joc? (da/nu): ").strip().lower()
        if nou_joc != 'da':
            print("Joc terminat. La revedere!")
            break


ruleaza_joc()