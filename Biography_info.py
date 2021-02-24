name = input("¿Cual es tu nombre?")#validación de solo letras.
Date = input("Dame el día, el mes y el año, solo en números, ejemplo: 29 01 2021")#validación de solo números.
Address = input("Dame la calle donde vives")#validación de solo letras y numeros.
Metas = input("Metas personales")#validación de solo letras.

print("-------------------------------------")
#name.isalpha()
#isdigist
#Condición 1--------------------
name2 = name.replace(" ","")
if name2.isalpha()==True:
    print(name)
else:
    print("Solo tienes que poner letras")

#Condición 2--------------------
Date2 = Date.replace(" ","")
if Date2.isdigit()==True:
    print(Date)
else:
    print("Solo tienes que poner números")

#Condición 3--------------------
Address2 = Address.replace(" ","")
if Address2.isalpha()==True:
    print(Address)
else:
    print("Solo números o letras")

#Condición 4--------------------
Metas2 = Metas.replace(" ","")
if Metas2.isalpha()==True:
    print(Metas)
else:
    print("Solo letras o números")