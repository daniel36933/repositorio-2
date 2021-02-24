import random

numero = random.randrange(1,7)
guess = int (input("Adivina el número entre el 1 al 7: "))
var = 0

while guess != numero:
    if guess < numero:
        print("Este no es el número. Prueba con otro")
        guess = int (input("\nAdivina el número entre el 1 al 7: "))
        var = var + 1
    else:
        print("Necesitas poner un número dentro del limite. Prueba de nuevo")
        guess = int (input("\nAdivina el número entre el 1 al 7: "))
        var = var + 1

print("Felicidades, tienes el número correcto")
print("Probaste en " + str(var) + " intentos")