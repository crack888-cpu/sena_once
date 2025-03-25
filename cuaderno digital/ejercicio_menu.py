def menu():
    print("""Menu:
          1. funcion validar username
          2. funcion validar passaword
          3. funcion registrar_usuario
          4. funcion mostrar_usuarios
          5. Saliendo""")
    def validar_username():
        print("Estas en la funcion validar username")
        return menu()

    def validar_password():
        print("Estas en la funcion validar password")
        return menu()

    def registrar_usuario():
        print("Estas en la funcion registrar usuario")
        return menu()

    def mostrar_usuarios():
        print("Estas en la funcion mostrar usuarios")
        return menu()
    
    op = int(input("$: "))
    while op == 1:
        opciones1 = lambda a = 1: validar_username()
        opciones1(op)
    while op == 2:
        opciones1 = lambda a = 1: validar_password()
        opciones1(op)
    while op == 3:
        opciones1 = lambda a = 1: registrar_usuario()
        opciones1(op)
    while op == 4:
        opciones1 = lambda a = 1: mostrar_usuarios()
        opciones1(op)
    while op == 5:
        print("Saliendo...")
        break
menu()
