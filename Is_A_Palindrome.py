var = 1

while var < 6:
    palabraNormal = input("Introduce la palabra #" + str(var))
    palabraInvertida = palabraNormal[::-1]

    if(palabraNormal == palabraInvertida):
        print("Loteria!!, la palabra es igual, tanto al derecho y al revez.")
        var = var + 1
    else:
        print("Esto no es un Palindrome.")
        var = var + 1