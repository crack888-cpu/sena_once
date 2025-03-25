#def saludar():
#    print("Hola, mundo")

# Llamar funcion
#saludar()

def validar(correo1, contra1):
    if correo1 == "cortesgmail.com" and contra1 == "12345":
        print("Bienvenido")
    else:
        print("Error")
        

correo = str(input("Correo: "))
contra = str(input("Contraseña: "))

validar(correo, contra)

