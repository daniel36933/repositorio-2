from random import randint
print("-------------------------------")

choice = ["rock", "paper", "scissors"]
def main():
    computer = choice[randint(0,2)]

    print("Bienvenido a Piedra, papel o tijera\n")
    jugador = input("Tu opción es: ").lower()
    print("La computadora selecciono: " + computer)


    if jugador == computer:
        print("Empate")
    elif jugador == "rock" and computer == "paper":
        print("La computadora gano")
    elif jugador == "rock" and computer == "scissors":
        print("Tu ganaste")
    elif jugador == "paper" and computer == "rock":
        print("Tu ganaste")
    elif jugador == "paper" and computer == "scissors":
        print("La computadora gano")
    elif jugador == "scissors" and computer == "rock":
        print("La computadora gano")
    elif jugador == "scissors" and computer == "paper":
        print("Tu ganaste")
    main()

main()