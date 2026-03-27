set_pare = {x for x in range(0, 20) if x % 2 == 0}
print("Primele 10 numere pare:", set_pare)

text1 = "inteligenta artificiala"
litere_distincte = {c for c in text1 if c != " "}
print("Litere distincte:", litere_distincte)

text2 = "ython este un limbaj de programare de nivel inalt, cu uz general si este unul dintre cele mai solicitate limbaje în zilele noastre."
cuvinte_lungi = {cuv for cuv in text2.split() if len(cuv) >= 5}
print("Cuvinte cu minim 5 litere:", cuvinte_lungi)
