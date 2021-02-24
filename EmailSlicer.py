correo = input("Introduce tu correo electrónico: ").strip()

#Extraemos el nombre de usuario
nombreUsuario = correo[:correo.index("@")]

#Extraemos el dominio del correo
dominio = correo[correo.index("@")+1:]

resultado = "Tu nombre de Usuario es: {}\nTu dominio es: {}".format(nombreUsuario, dominio)
print(resultado)

