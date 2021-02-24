acrom = input("Escribe una frase y te dire el acronimo")
#ac = acrom.upper()
#--------------------------------
acrom2 = ''
for c in acrom:
    if c.isupper():
        acrom2 += c

print(acrom2)