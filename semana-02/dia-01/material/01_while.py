

password = ""
valido    = True


while valido == True:
    password = input("Ingrese la contraseña correcta: ")
    if password == "python":
        valido = False

print("Contraseña correcta, acceso concedido.")
