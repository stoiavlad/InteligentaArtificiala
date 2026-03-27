data = "2004-13-08 12:09:52.749678"

extrage = lambda d: (d.split(" ")[0].split("-")[0],
                     d.split(" ")[0].split("-")[1],
                     d.split(" ")[0].split("-")[2],
                     d.split(" ")[1])

an, luna, zi, ora = extrage(data)

print(an)
print(luna)
print(zi)
print(ora)