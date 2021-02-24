opc = int(input("\nMenú\n-----------------------------------\n\t" +
            "Con número selecciona a tu artista preferido\n\t1.Pedro Infante\n\t2.Maluma\n\t3.Shakira\n\t4.Salir\n\n\t"))

while(opc > 0 and opc < 5):
    if(opc == 1):
        opc1 = int(input("\nElige alguna de sus 3 canciones\n\t" +
                    "1.Cien años\n\t2.No volveré\n\t3.La calandria\n\t4.Salir\n"))
        if(opc1 == 1):
            print("-----Cien años-----\n\tPasaste a mi lado\n\tCon gran indiferencia\n\tTus ojos ni siquiera\n\tVoltearon hacia mí")
            break
        elif(opc1 == 2):
            print("-----No volveré-----\n\tCuando lejos me encuentre de ti\n\tCuando lejos me encuentre de ti\n\tNo hallarás un recuerdo de mí\n\tNi tendrás más amores conmigo")
            break
        elif(opc1 == 3):
            print("-----La calandria-----\n\tNi tendrás más amores conmigo\n\tPendiente de un balcón\n\tSe hallaba una calandria\n\tCantando su dolor")
            break
        elif(opc1 == 4):
            break
    elif(opc == 2):
        print("-----Maluma-----\n\tDeja de mentirte (ah)\n\tLa foto que subiste con él diciendo que era tu cielo\n\tBebé, yo te conozco tan bien, sé que fue pa' darme celos\n\tNo te diré quién, pero llorando por mí te vieron\n\tPor mí te vieron")
        break
    elif(opc == 3):
        print("-----Shakira-----\n\tYou're a good soldier\n\tChoosing your battles\n\tPick yourself up and dust yourself off\n\tAnd back in the saddle")
        break
    elif(opc == 4):
        break
else:
    print("Favor de ingresar solo opciones validas")