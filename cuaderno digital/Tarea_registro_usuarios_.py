usuarios = []

def main():
    op = 0
    while op != 3:
        try:
            print("""\n----Sistema de registros----\nElige una opción:\n1. Registrar usuario\n2. Ver usuarios\n3. Salir""")
            opciones = {1: registrar_usuario,
                        2: mostrar_usuarios,
                        3: lambda : print("Saliendo del sistema...")}
            op = int(input("Elige una opción: "))
            opciones.get(op, lambda : print("Opción incorrecta. Vuelve a ingresar una opción"))()
        except ValueError:
            print("¡ERROR!: Ingresa un número válido.")

def validar_username(username):
    return any(username == user["Username"] for user in usuarios)

def validar_password(password):
    return len(password) >= 6

def registrar_usuario():
    username = str(input("Registra tu username: "))
    while validar_username(username):
        username = str(input("¡Usuario Existente!\nRegistra un username de nuevo: "))
    password = str(input("Registra tu password: "))
    while not validar_password(password):
        password = str(input("Registra tu password de nuevo con al menos 6 caracteres: "))
    email = str(input("Registra tu email: "))
    while not ("@" in email and "." in email and email.find("@") < email.rfind(".") 
               and email.find("@") > 0 and email.rfind(".") < len(email) - 1 
               and ((email.rindex(".") - email.index("@")))>=5):
        email = str(input("Email inválido (recuerda usar primero @ y después el punto. EJ: luis@gmail.com): "))
    while True:
        try:
            edad = int(input("Registra tu edad: "))
            while edad < 0:
                edad = int(input("Registra una edad correcta positiva: "))
            break 
        except ValueError:
            print("Ingresa una edad numérica válida.")
    diccionario = {"Username": username, "Password": password, "Email": email, "Edad": edad}
    usuarios.append(diccionario)
    print("Usuario registrado con éxito.")

def mostrar_usuarios():
    print(f"La lista de usuarios es:\n{usuarios} ")
    
main()