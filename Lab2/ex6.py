print("Bine ai venit in padurea magica!")

inventar = []

alegere1 = input("Mergi la stanga sau la dreapta? ")

if alegere1 == "stanga":
    print("Ai intalnit un lup!")

    alegere2 = input("Fugi sau lupti? ")

    if alegere2 == "lupti":
        print("Ai invins lupul!")
        inventar.append("blana de lup")
    else:
        print("Ai fugit si ai pierdut ceva timp.")

elif alegere1 == "dreapta":
    print("Ai gasit un cufar!")

    alegere2 = input("Il deschizi? (da/nu) ")

    if alegere2 == "da":
        print("Ai gasit o comoara!")
        inventar.append("aur")
    else:
        print("Ai plecat mai departe.")

else:
    print("Nu ai ales corect!")

print("Mai mergi putin si gasesti o poțiune magica.")
alegere3 = input("O iei? (da/nu) ")

if alegere3 == "da":
    inventar.append("potiune")
    print("Ai luat potiunea!")
else:
    print("Ai lasat-o acolo.")

print("Aventura s-a terminat!")
print("Inventarul tau:", inventar)