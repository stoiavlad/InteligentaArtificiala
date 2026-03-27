dict_patrate = {x: x**2 for x in range(1, 11)}
print("Numere si patrate:", dict_patrate)

text = "inteligenta artificiala"
frecventa_litere = {c: text.count(c) for c in text if c != " "}
print("Frecventa litere:", frecventa_litere)

divizori = {x: [d for d in range(1, x + 1) if x % d == 0] for x in range(1, 11)}
print("Divizori:", divizori)
