def genereaza_factura(nume_client, **produse):
    print("Factura pentru:", nume_client)

    total = 0

    for produs in produse:
        pret = produse[produs]
        print(produs, "-", pret, "RON")
        total = total + pret

    print("Total:", total, "RON")


genereaza_factura(  "Vlad", faina=3, zahar=6, orez=15)