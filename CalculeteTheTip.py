subtotal = float (input("¿Cuál es la factura de hoy?"))
personas = int (input("¿Cuantas personas involucradas hay?"))

pro1 = ((subtotal*18)/100)/personas
pro2 = ((subtotal*20)/100)/personas
pro3 = ((subtotal*25)/100)/personas
pro_1 = (subtotal*18)/100
pro_2 = (subtotal*20)/100
pro_3 = (subtotal*25)/100
total1 = (subtotal + pro_1)/personas
total2 = (subtotal + pro_2)/personas
total3 = (subtotal + pro_3)/personas

#Variables con números redondeados
var1 = round(pro1)
var2 = round(pro2)
var3 = round(pro3)
var4 = round(total1)
var5 = round(total2)
var6 = round(total3)


print("El total de la factura es: " + str(subtotal))
print("La propina para el 18 porciento de cada mesero es: " + str(var1) + " lo que eleva a un total para cada uno: " + str(var4))
print("La propina para el 20 porciento de cada mesero es: " + str(var2) + " lo que eleva a un total para cada uno: " + str(var5))
print("La propina para el 25 porciento de cada mesero es: " + str(var3) + " lo que eleva a un total para cada uno: " + str(var6))